#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    for (int len = 1; len <= n; len++)
    {
        for (int i = 0; i + len <= n; i++)
        {
            int unique = 1;
            for (int j = 0; j + len <= n; j++)
            {
                if (j == i)
                {
                    continue;
                }
                int same = 1;
                for (int k = 0; k < len; k++)
                {
                    if (arr[i + k] != arr[j + k])
                    {
                        same = 0;
                        break;
                    }
                }
                if (same)
                {
                    unique = 0;
                    break;
                }
            }
            if (unique)
            {
                printf("%d\n", len);
                return 0;
            }
        }
    }
    return 0;
}