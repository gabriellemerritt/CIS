#include <stdio.h>
#include <stdlib.h> 
#include <time.h> 
#include "../inc/Magicsquare.h" 




int main()
{ 
	MagSquare_PTR mpoint; 
	mpoint = (MSQUARE_TYPE*)malloc(sizeof(MSQUARE_TYPE *) *MAGICSIZE* MAGICSIZE); // malloc something to create space to point at 
	// for ( int i = 0; i < MAGICSIZE; i++)
	// {
	// 	mpoint[i] = (MSQUARE_TYPE*)malloc(MAGICSIZE * sizeof(MSQUARE_TYPE)); 
	// }

	initSquare(*mpoint, MAGICSIZE); 
	if (isMagic(*mpoint,MAGICSIZE) == 1){
		printf ("\n~~magic square~~\n ");
	}
	else{
		printf ("\nYour square is not a magic square\n");
	}
	printSquare(*mpoint, MAGICSIZE); 
	
	
}

