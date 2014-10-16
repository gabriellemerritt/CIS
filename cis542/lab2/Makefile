# Makefile by Gabrielle Merritt for CIS542 
# Please only run .bin files 

BINDIR=bin
OUT1= $(BINDIR)/magicSquare_part1.bin
OUT2= $(BINDIR)/magicSquare_part2.bin
SRC =src/
CFLAGS= -Wall -g
CC= gcc

default: ${BINDIR} $(OUT1) $(OUT2)
${BINDIR}:
	mkdir -p ${BINDIR}

$(OUT1): $(SRC)Maintest1.c
	$(CC) -o $(OUT1) $(SRC)Magicsquare1.c $(SRC)Maintest1.c $(CFLAGS)

$(OUT2): $(SRC)maintest2.c
	$(CC) -o $(OUT2) $(SRC)magicsquare2.c $(SRC)maintest2.c $(CFLAGS)
	
clean:
	rm -r $(BINDIR)
	 
	