/* finding the larger of two numbers */

#include <stdio.h>

int main(void)
{
    /* the two numbers */
    int number1, number2;

    /* we will save the larger number here */
    int max;

    /* read two numbers */
    scanf("%d", &number1);
    scanf("%d", &number2);

    /* we temporarily assume that the first number is the larger one */
    /* we will check it soon */
    max = number1;

    /* we check if the assumption was true */
    if(number2 > max)
    max = number2;

    /* we print the result */
    printf("The largest number is %d \n",max);

    /* we finish the program successfully */
    return 0;
}