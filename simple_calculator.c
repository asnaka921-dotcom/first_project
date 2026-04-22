#include<stdio.h>
int main()
{
	int num1,num2,ans;
	char operator;
	printf("enter 2 numbers:\n");
	scanf("%d%d",&num1,&num2);
	printf("enter an arithmetic opertor:\n");
	scanf(" %c",&operator);
	switch(operator)
	{
		case'+':ans=num1+num2;
			printf("%d + %d = %d\n",num1,num2,ans);
			break;
		case'-':ans=num1-num2;
			printf("%d - %d = %d\n",num1,num2,ans);
			break;
		case'*':ans=num1*num2;
			printf("%d * %d = %d\n",num1,num2,ans);
			break;
		case'/':ans=num1/num2;
			printf("%d / %d = %d\n",num1,num2,ans);
			break;
		
		default:printf("invalid input\n");
	}
	return 0;
}
