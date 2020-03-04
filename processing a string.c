#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
	int t;
	char s[1000];
    int i,sum=0,v;
	printf("Enter the number of test cases: ");
	scanf("%d",&t);
	while(t--)
    {
        printf("Enter the string to be entered: ");
        scanf("%s",&s);
        int c=strlen(s);
        for(i=0;i<c;i++)
        {
            if(s[i]<58&&s[i]>47)
            {
                v=s[i] - '0';
                sum=sum+v;
            }
        }
        printf("%d\n",sum);
    }

    return 0;
}

