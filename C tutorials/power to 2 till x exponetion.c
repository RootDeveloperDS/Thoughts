#include <stdio.h>

int main(void) {
    int exp;
    int pow = 1;

    for(exp = 0; exp < 16; exp++) {
    printf("2 to the power of %d is %d\n", exp, pow);
        pow *= 2;
    }
    return 0;
}