
#include "../inc/prime.h"

int is_prime(int n) // returns 0 if number is not a prime  1 if a prime number 
{
	int k, limit; // set 
	if (n==2) // if number is 2 then only one prime which is 1 
	{
	 return 1;
	}

	if (n % 2 == 0) // if number is even it is not a prime number
	{
	 return 0;
	}

	limit = n/2; // 

	for( k = 3; k <= limit; k+=2 ) // starting at 3 counting every odd number and checking to make sure its not divisible by another number 
	{
		if ( n % k == 0)
		{
			return 0;
		}
	}
	return 1;
}