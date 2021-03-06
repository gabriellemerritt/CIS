/*
	Gabrielle Merritt 
	CIS542 
	gmerritt@seas.upenn.edu 
	Lab 1 
*/
#include "../inc/simple_c.h"
#include <stdio.h> 
#include <string.h>
#include <stdlib.h> 

#define MAX_BUFFER 1024
int name_length =0;

int main (int argc, char* argv[])
{
	parseName(argv,(argc));  
	
	//printf("%s", argv[1]);
	

	return 0; 
}
void parseName(char* argv[], int length)
{
	printf("\n");
	for(int i = 1; i < length; i++)
	{
		char* str; 
		str = (char*)malloc(sizeof(char)*100); 
		strcpy(str, *(argv+i));
		name_length = reverseString(str); // calls reverse string which returns length of string 
		printf("%s ",str);
		fflush(stdout); 
		free(str); 
	}
	printf("\n");
	printf("name length is : %i\n",name_length );
}

int reverseString(char* buffer_point)
{
	char *t; 
	t = buffer_point;
	char temp; 
	while( *t != '\0'){
		name_length++;
		t++; 

	}
	t--; 
	while (t > buffer_point)
	{
		temp = *buffer_point; 
		*buffer_point = *t; 
		*t = temp; 
		t--; 
		buffer_point++; 
	}
	return name_length; 
}
