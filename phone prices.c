#include<stdio.h>
int main()
{
    int t,c=1,i,n,price[10000],min,a=0;
    printf("Enter the number of test cases: ");
    scanf("%d",&t);
    printf("Enter the number of days: ");
    scanf("%d",&n);
    while(t--)
    {
        for(i=1;i<=n;i++)
        {
            scanf("%d",&price[i-1]);
        }
        min=price[0];
        for(i=1;i<n;i++)
        {
            if(min>price[i])
            {
                min=price[i];
                c++;
            }
        }
        for(i=1;i<n-1;i++)
        if(price[n-1]<price[i])
        {
            a++;
        }
        if(a==n-2)
        {
            c++;
        }

    }
    printf("Good days: %d",c);
}
