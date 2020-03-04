#include<stdio.h>
int main()
{
    int t,l,r,c=0,i,rem;
    printf("Enter the number of test cases" );
    scanf("%d",&t);
    while(t--)
    {
        c=0;
        printf("Enter the left and right value: ");
        scanf("%d %d",&l,&r);
        for(i=l;i<=r;i++)
        {
            rem=i%10;
            if(rem==2||rem==3||rem==9)
            {
                c++;
            }
        }
        printf("%d",c);
    }
}
