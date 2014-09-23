
/*
	Gabrielle Merritt 
	CIS542 
	gmerritt@seas.upenn.edu 
	Lab 1 
*/
#include "../inc/prime.h"
#include <stdio.h> 
#include <stdlib.h>  

int main()
{
	int number; 
	int number_prime = 0; // initially guessing its not a prime number 
	printf("\nplease enter an integer!\n"); 
	scanf("%i", &number); 
	number_prime = is_prime(number); // will be 0 if a prime numbe r
	printf("\n");
	for (int i = 0; i < number; i++)
	{
		if (is_prime(i) == 1)
		{
			printf ("%i\n", i); 
		}
	}
	if (number_prime == 1)
	{
		printf("%i\n",number); 
	}
	return 0; 
}