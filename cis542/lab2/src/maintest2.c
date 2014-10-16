#include <stdio.h>
#include <stdlib.h> 
#include <time.h> 
#include "../inc/magicsquare2.h" 




int main()
{ 
	int M = MAGICSIZE*(MAGICSIZE*MAGICSIZE +1)/2;
	int count = 0; 
	MagSquare_PTR mpoint; 
	mpoint = (MSQUARE_TYPE*)malloc(sizeof(MSQUARE_TYPE *) *MAGICSIZE* MAGICSIZE); // malloc something to create space to point at 
	// for ( int i = 0; i < MAGICSIZE; i++)
	// {
	// 	mpoint[i] = (MSQUARE_TYPE*)malloc(MAGICSIZE * sizeof(MSQUARE_TYPE)); 
	// }

	initSquare(*mpoint, MAGICSIZE); 
	printf("\nMagic number for this %d x %d square is %d\n",MAGICSIZE,MAGICSIZE,M);

	printSquare(*mpoint,MAGICSIZE); 
	if (isMagic(*mpoint,MAGICSIZE) == 1){
		printf ("\n~~magic square~~\n ");

		printSquare(*mpoint, MAGICSIZE); 
		return 0; 
	}
	// srand(time(NULL));
	while(1)
	{
		if(isMagic(*mpoint,MAGICSIZE) ==1){
			printf("Number of entries switched %d",count); 
			printSquare(*mpoint, MAGICSIZE);
			return 0; 
		}
		permuteSquare(*mpoint);  
		printSquare(*mpoint, MAGICSIZE);
		count ++; 
	}


	
}
	 
	
	


