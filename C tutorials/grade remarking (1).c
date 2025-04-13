#include <stdio.h>

int main()
{
	/* your code */
	float floating;
	scanf("%f",&floating);
	(int) floating;
	if(floating>=1 && floating <2) {
	    puts("very bad");
	}
	else if(floating>=2 && floating <3 ) {
	    puts("Bad");
	}
	else if(floating>=3 && floating <4) {
	    puts("Neutral");
	}
	else if(floating>=4 && floating <5) {
	    puts("good");
	}
	return 0;
}