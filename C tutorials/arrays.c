#include <stdio.h>

int main()
{
    /*{
        int numbers[5],i;   //array or vector of 5 ariables of value integer
        numbers[0]=111;   //assigning 111 to 0 index
        i=numbers[2];  //assigning value to i
        numbers[1]=numbers[4];   //assigning value of 5th to 2nd variable

    }*/
    int numbers[5], sum = 0, i;

    for (i = 0; i < 5; i++)
    {
        sum += numbers[i]; // sum of all values inside this array
        
    }
}