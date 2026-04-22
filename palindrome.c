#include <stdio.h>
int main()
{
    int n, original, rev = 0, remainder;
    printf("Enter a number: ");
    scanf("%d", &n);
    original = n;

    while (n != 0)
    {
        remainder = n % 10;
        rev = rev * 10 + remainder;
        n/= 10;
    }

    if (original == rev)
        printf("Palindrome\n");
    else
        printf("Not Palindrome\n");

    return 0;
}

