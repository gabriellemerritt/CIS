#include <stdio.h>
#include <stdlib.h> 
#include <time.h> 
#include "Magicsquare.h" 


#define MAGICSIZE 3 

typedef int MSQUARE_TYPE[MAGICSIZE][MAGICSIZE]; 
typedef MSQUARE_TYPE * MagSquare_PTR; 
void initSquare(MagSquare_PTR, int magicsquaresize); 
void printSquare(MagSquare_PTR, int magicsquaresize); 

int main(){ 
	srand(time(NULL)); // seed random time generator 
	MagSquare_PTR mptr = // malloc something to create space to point at 
	initSquare(mptr, MAGICSIZE); 
	printSquare(mptr, MAGICSIZE); 
}

