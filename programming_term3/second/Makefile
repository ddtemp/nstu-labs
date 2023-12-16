CC = gcc
CFLAGS = -Wall -shared
EXE_CFLAGS = -Wall -Wextra -Werror

all: lib.so main.out

lib.so: lib.c
	$(CC) $(CFLAGS) -o lib.so lib.c

main.out: main.c lib.so
	$(CC) $(EXE_CFLAGS) -o main.out main.c -ldl

clean:
	rm -f lib.so main.out

