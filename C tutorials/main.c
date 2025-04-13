#include <stdio.h>
int main(void)
{
    int a, b;
    a = 4;
    b = 3 * a;
    printf("It's working\n%d\n%d\n", a, b);
    return 0;
}
int sum()
{
    int position;
    scanf("%d", &position);
    switch (position)
    {
    case 1:
        printf("value is %d", position);
        break;
    default:
        break;
    }
    return 0;
}