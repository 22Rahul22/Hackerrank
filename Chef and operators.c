#include<stdio.h>
int main()
{
    int t,a,b;
    printf("Enter the number of test cases: ");
    scanf("%d",&t);
    while(t--)
    {
        printf("Enter the numbers: ");
        scanf("%d %d",&a,&b);
        if(a<b)
            printf("<\n");
        else if(a>b)
            printf(">\n");
        else
            printf("=\n");
    }
}
