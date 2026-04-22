#include<stdio.h>
#include<string.h>
#include<ctype.h>
int main()
{
    char str[50],i;
    printf("enter the string");
    scanf("%s",str);
    for(int i=0;str[i]!=0; i++)
        str[i]=tolower(str[i]);
        printf("string in lower case=%s",str);
    
    return 0;
}


