#include<stdio.h>
int main()
{
    int t,n,*arr1,*arr2,i=0,j,c=0,k;
    printf("\n\nEnter the number of test cases: ");
    scanf("%d",&t);
    while(i<t)
    {
        printf("Enter the size of array: ");
        scanf("%d",&n);
        arr1=(int *)malloc(n*sizeof(int));
        arr2=(int *)malloc(n*sizeof(int));
        for(j=0;j<n;j++)
        {
            scanf("%d",(arr1+j));
        }
        for(j=0;j<n;j++)
        {
            c=0;
            for(k=0;k<n;k++)
            {
                if(*(arr1+j)<*(arr1+k))
                {
                    c++;
                }
            }
            *(arr2+j)=c;
        }
        for(j=0;j<n;j++)
        {
            printf("%d ",*(arr2+j));
        }
        i++;
    }
}
