#include <stdio.h>
#include <stdlib.h> 
#include <time.h> 
#include "../inc/magicsquare2.h" 

void initSquare(MSQUARE_TYPE MagSquare_PTR, int magicsquaresize) 
{
	int squaresize = magicsquaresize*magicsquaresize; 
	int i,j,k,temp; 
	int p = 0; 
	srand(time(NULL));
	int magic_numbers[squaresize]; 
	
	for(i = 0; i < squaresize; i++)
	{
		magic_numbers[i] = i+1;  
	}

	for (j = (squaresize -1); j>=1; j--)
	{

		k = rand() % j+1; 
		temp = magic_numbers[j]; 
		magic_numbers[j] = magic_numbers[k]; 
		magic_numbers[k] = temp; 

	}

	for (int l = 0; l < magicsquaresize; l ++)
	{
		//printf("%d", magic_numbers[l]); 
		for (int m = 0; m < magicsquaresize; m++ )
		{
			MagSquare_PTR[l][m] = magic_numbers[p]; 
			p++;
		}
	}
}
	
void printSquare(MSQUARE_TYPE MagSquare_PTR, int magicsquaresize)
{
	printf("\n");
	for (int i = 0; i < magicsquaresize; i ++)
	{
		for (int j = 0; j < magicsquaresize; j++ )
		{
			printf("%d",MagSquare_PTR[i][j]); 
			printf(" ");			

		}
		
		printf("\n");
	}
	printf("\n");



}
int sumColumn (int column, MSQUARE_TYPE MagSquare_PTR, int size) // column number from 0 -> n-1 
{
	int sum = 0; 
	for(int i = 0; i < size; i++)
	{
		sum += MagSquare_PTR[column][i];
	}
	// printf("\nColumn %d sum is %d",column,sum); 
	return sum; 
}
int sumRow(int row, MSQUARE_TYPE MagSquare_PTR, int size)
{
	int sum = 0; 
	for(int i = 0; i < size; i++)
	{
		sum += MagSquare_PTR[i][row];
	}
	// printf("\nRow %d sum is %d",row,sum); 
	return sum; 
	
}
int sumDiagonal(int diagonal, MSQUARE_TYPE MagSquare_PTR, int size)
{
	int sum = 0; 
	if (diagonal == 0){
		for(int i = 0; i < size; i++)
		{
			sum += MagSquare_PTR[i][i]; 
		}
	}
	else{
		for(int j = 0; j< size ; j++)
		{
			sum +=MagSquare_PTR[j][(size -1 -j)];
		}
	}
	// Diagonal = 1 is top right to bottom left 
	// printf("\nDiagonal %d sum is %d",diagonal,sum); 
	return sum;
}
int isMagic(MSQUARE_TYPE MagSquare_PTR, int size)
{
	int shape = size*size; 
	int sum = (size*(shape +1))/2; 
	int temp1 = 0;
	int temp2  = 0; 
	int truth = 0; 
	for(int i = 0; i< size; i++)
	{
		temp1 = sumRow(i,MagSquare_PTR,size);
		temp2 = sumColumn(i,MagSquare_PTR,size);
		if ((temp1 == sum) && (temp2 == sum))
		{
			truth = 1; 
		}
		else {
			truth = 0; 
		}
	}
	if((sumDiagonal(0,MagSquare_PTR,size) == sum) && (sumDiagonal(1,MagSquare_PTR,size) == sum))
	{
		truth = 1;
	}
	else{
		truth= 0; 
	}
	return truth; 
}
void testMagic (MSQUARE_TYPE MagSquare_PTR)
{
	int p = 0; 
	int magicsquare[9] = {2,7,6,9,5,1,4,3,8}; 
	for(int i = 0; i< 3; i++)
	{
		for(int j = 0; j < 3; j++)
		{
			MagSquare_PTR[i][j] = magicsquare[p]; 
			p++; 
		}
	}
}
void permuteSquare(MSQUARE_TYPE MagSquare_PTR)
{
	// int used[256];
	int j; 
	int k; 
	int temp;   
	int squaresize = MAGICSIZE; 
	j = rand() % (squaresize);
	k = rand() % (squaresize); 
	if (j == (1)){
	k = j+1; 
	}
	// else{
	// 	k = j-1; 
	// }
	// //printf("\nj = %d\nk =%d",j,k); 
	temp = MagSquare_PTR[k][j];  
	MagSquare_PTR[k][j] = MagSquare_PTR[1][1]; 
	MagSquare_PTR[1][1] = temp; 


	
	
}
//void magicShuffle(MagSquare_PTR MagSquare_PTR, int squaresize)



