CC = gcc
CFLAGS = -Wall -shared

all: lib.so child.out

lib.so: lib.c
	$(CC) $(CFLAGS) -o lib.so lib.c

child.out: child.c main.c 
	$(CC) -o main child.c main.c

clean:
	rm -f lib.so main
	rm -f *.new
