#include<stdio.h>
#include<string.h>
int main()
{
    int t,z;
    char h[100];
    printf("Enter the number of test cases: ");
    scanf("%d",&t);
    while(t--)
    {
        printf("Enter the hour: ");
        scanf("%s",&h);
        z=h[0]-'0';
        printf("Value: %d",z);
    }
}
