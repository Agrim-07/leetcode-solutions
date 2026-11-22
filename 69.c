#include <stdio.h>

int main()
{
    int x;
    scanf("%d", &x);
    long long a = 0;
    while (a * a <= x)
    {
        a++;
    }
    printf("%lld\n", a - 1);
    return 0;
}