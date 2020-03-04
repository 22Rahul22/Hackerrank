#include<stdio.h>
int main()
{
    long long int i,c=0,t,r;
    printf("Enter the number of test cases: ");
    scanf("%lld",&t);
    while(t--)
    {
        printf("\nEnter the number: ");
        scanf("%lld",&num);
        c=0;
        while(num!=0)
        {
            r=num%10;
            if(r==4)
            {
                c++;
            }
            num=num/10;
        }
        printf("\n%lld",c);
    }
}
