#include <dlfcn.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int child_main(int argc, char *argv[]) {
    char *fileNameWithExtension = argv[1];
    char toDelete = *argv[2];

    if (scanf("%s %c", fileNameWithExtension, &toDelete) != 2) {
        printf("Failed to read arguments from input\n");
        return -1;
    }

    char fileNameWithoutExtension[256];
    size_t len = strlen(fileNameWithExtension);
    size_t dotIndex = len;
    for (size_t i = len - 1; i > 0; i--) {
        if (fileNameWithExtension[i] == '.') {
            dotIndex = i;
            break;
        }
    }

    strncpy(fileNameWithoutExtension, fileNameWithExtension, dotIndex);
    fileNameWithoutExtension[dotIndex] = '\0';

    int inputFile = open(fileNameWithExtension, O_RDONLY);
    if (inputFile < 0) {
        printf("Failed to open file\n");
        return -1;
    }

    char destinationFileName[strlen(fileNameWithoutExtension)];
    strcpy(destinationFileName, fileNameWithoutExtension);
    int outputFile = creat(
        strncat(destinationFileName, ".new",
                sizeof(destinationFileName) - strlen(destinationFileName) - 1),
        O_WRONLY | S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH);
    if (outputFile < 0) {
        printf("Failed to write to %s\n", destinationFileName);
        return -1;
    }

    int result = 0;
    void *handle;
    handle = dlopen("./lib.so", RTLD_LOCAL | RTLD_NOW);
    if (handle) {
        int (*func)(int, int, char);
        *(void **)(&func) = dlsym(handle, "deleteChar");
        if (func) {
            result = (*func)(inputFile, outputFile, toDelete);

            // Convert the number of changes to a string
            char changes_str[64];
            snprintf(changes_str, sizeof(changes_str), "%d", result);

            // Send the number of changes back to the parent process
            write(STDOUT_FILENO, changes_str, strlen(changes_str));
        } else {
            printf("Failed to find function\n");
            return -1;
        }
        dlclose(handle);
    } else {
        printf("Failed to load library\n");
        return -1;
    }

    close(inputFile);
    close(outputFile);

    return 0;
}
