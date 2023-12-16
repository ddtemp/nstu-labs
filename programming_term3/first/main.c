#include <fcntl.h>
#include <stdio.h>
//#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
  if (argc != 3) {
    printf("Wrong arguments count\n");
    return -1;
  }

  char *fileName = argv[1];
  char toDelete = *argv[2];

  int inputFile = open(fileName, O_RDONLY);
  if (inputFile < 0) {
    printf("Failed to open file\n");
    return -1;
  }

  char destinationFileName[strlen(fileName) + 11];
  strcpy(destinationFileName, fileName);
  int outputFile = creat(strcat(destinationFileName, ".helpmepls"), O_WRONLY);
  if (outputFile < 0) {
    printf("Failed to write to %s\n", destinationFileName);
    return -1;
  }

  int deletions = 0;
  int c;
  while (read(inputFile, &c, 1)) {
    if (c != toDelete) {
      write(outputFile, &c, 1);
    } else {
      deletions++;
    }
  }

  if (chmod(destinationFileName, S_IRUSR | S_IWUSR) == -1) {
    perror("chmod");
    return -1;
  }

  close(inputFile);
  close(outputFile);

  return deletions;
}