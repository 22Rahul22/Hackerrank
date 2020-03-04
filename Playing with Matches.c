#include<stdio.h>
int main()
{
    int t,a,b,r,x,sum=0;
    printf("Enter the number of test cases: ");
    scanf("%d",&t);
    while(t--)
    {
        printf("Enter two numbers: ");
        scanf("%d %d",&a,&b);
        a=a+b;
        sum=0;
        while(a>0)
        {
            r=a%10;
            if(r==0||r==9||r==6)
                x=6;
            else if(r==1)
                x=2;
            else if(r==2||r==3||r==5)
                x=5;
            else if(r==4)
                x=4;
            else if(r==7)
                x=3;
            else
                x=7;
            sum=sum+x;
            a=a/10;
        }
        printf("%d",sum);
    }
}
