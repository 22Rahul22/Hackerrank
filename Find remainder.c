#include<stdio.h>
int main()
{
    int t,a,b,r;
    printf("Enter the number of test cases: ");
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d %d",&a,&b);
        r=a%b;
        printf("%d",r);
    }
}
