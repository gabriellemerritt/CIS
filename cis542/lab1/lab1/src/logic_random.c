/*
	Gabrielle Merritt 
	CIS542 
	gmerritt@seas.upenn.edu 
	Lab 1 
*/
#include "../inc/logic_random.h"
#include <stdio.h>
#include <time.h> 
#include <string.h> 
#include <stdlib.h> 



int fail;
int main()
{
	srand(time(NULL)); 
	int luckynumber = rand() % 100 +1; 
	int guess = 0; 
	
 
	time_t current;
    struct tm * info;

  	time (&current);
    info = localtime (&current);
	
	printf("\nCurrent time is: %s, Pick a number between 1 and 100!\n ",asctime(info));
	time_t start;
	time(&start);
	if (guessResolver(luckynumber, guess,(int)start) == 1)
	{
		time_t end;
		time(&end); 
		printf ("Out of guesses :(, time is: %i \n", timeDif((int)start,(int)end)); 
	}
}

int guessResolver(int luckynumber, int guess, int start)
{
	scanf("%i", &guess); 
	for (int i = 0; i < MAX_GUESS; i++)
	{ 
		if((guess - luckynumber) == 0 )
		{
			time_t end; 
			time(&end); 
			printf("Correct! %i is the random number\n", guess);
			printf("it took you %i seconds to find the random number!\n", timeDif(start,(int)end)); 
			i = MAX_GUESS- 1;
			return 0;  

		}
		else if (((guess -luckynumber) <= 10) && ((guess - luckynumber) > 0))
		{
			printf("The number is slightly less than your guess, please guess again\n"); 
			scanf("%i",&guess); 
		}
		else if ((guess - luckynumber > 10))
		{
			printf("The number is much less than your guess, please guess again\n"); 
			scanf("%i",&guess); 
		}
		else if (((luckynumber - guess) <= 10) && ((luckynumber - guess) > 0))
		{
			printf("The number is slightly larger than your guess, please guess again\n"); 
			scanf("%i",&guess); 
		}
		else{
			printf("The number is much larger than your guess, please guess again \n"); 
			scanf("%i",&guess); 
		}

	}
	return 1; 
}
int timeDif(int start, int end)
{
	return (end - start); 
}