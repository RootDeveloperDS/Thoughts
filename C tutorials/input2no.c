#include <stdio.h>

int main(void) 
{
	int input1;
	int input2 = -1;
	while(input2 != 0)
	{
		scanf("%d", &input1);
		scanf("%d", &input2);
		printf("Sum: %d\n", input1 + input2);
	}
	if(input1==99)
		puts("Finish.");
	return 0;
}