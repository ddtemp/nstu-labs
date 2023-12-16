CC = gcc
CFLAGS = -Wall -shared
EXE_CFLAGS = -Wall -Wextra -Werror

all: lib.so child.out

lib.so: lib.c
	$(CC) $(CFLAGS) -o lib.so lib.c

child.out: child.c main.c 
	$(CC) $(EXE_CFLAGS) -o child.out child.c main.c

clean:
	rm -f lib.so child.out
