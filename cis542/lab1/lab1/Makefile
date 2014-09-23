# Makefile by Gabrielle Merritt for CIS542 
# Please only run .bin files 

BINDIR=bin
OUT1= $(BINDIR)/simple_c.bin
OUT2 = $(BINDIR)/logic_random.bin
OUT3 = $(BINDIR)/prime.bin 
SRC =src/
CFLAGS= -Wall -g
CC= gcc

default: ${BINDIR} $(OUT1) $(OUT2) $(OUT3)

${BINDIR}:
	mkdir -p ${BINDIR}

$(OUT1): $(SRC)simple_c.c
	$(CC) -o $(OUT1) $(SRC)simple_c.c $(CFLAGS)

$(OUT2): $(SRC)logic_random.c
	$(CC) -o $(OUT2) $(SRC)logic_random.c $(CFLAGS)

$(OUT3): $(SRC)step3.c $(SRC)prime.c
	$(CC) -o $(OUT3) $(SRC)step3.c $(SRC)prime.c $(CFLAGS)

clean:
	rm -r $(BINDIR)
	 
	