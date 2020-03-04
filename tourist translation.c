#include<stdio.h>
#include<string.h>
int main()
{
    int t,z,i;
    char s[100],byt[100];
    printf("Enter the number of test cases: ");
    scanf("%d",&t);
    printf("Enter the Bytelandian string: ");
    scanf("%s",&s);
    while(t--)
    {
        scanf("%s",&byt);
        printf("Translated string: ");
        for(i=0;i<strlen(byt);i++)
        {
            if(byt[i]>96&&byt[i]<123)
            {
                z=byt[i]-97;
                printf("%c",s[z]);
            }
            else if(byt[i]>64&&byt[i]<91)
            {
                z=byt[i]-65;
                printf("%c",s[z]-32);
            }
            else if(byt[i]=='_')
                printf(" ");
            else
                printf("%c",byt[i]);
        }
        printf("\n");
    }
}
