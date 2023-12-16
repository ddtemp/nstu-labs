#include <dlfcn.h>
#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <sys/stat.h>
#include <unistd.h>

int child_main(int argc, char *argv[]) {
  if (argc < 3) {
    printf("Arguments not specified or not complete\n");
    return -1;
  }

  char *fileNameWithExtension = argv[1];
  char toDelete = *argv[2];

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
      S_IRUSR | S_IWUSR);
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
    } else {
      printf("Failed to find function\n");
      return -1;
    }
    dlclose(handle);

  } else {
    printf("Failed to load library\n");
    return -1;
  }

  // if (chmod(destinationFileName, S_IRUSR | S_IWUSR) == -1) {
  //  perror("chmod");
  //  return -1;
  // }

  close(inputFile);
  close(outputFile);

  return result;
}