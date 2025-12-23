# include <stdio.h>
int main (){
    int a[]={};
    int i;
    int j;
        printf("input size of the array \n");
        scanf("%d",&j);
        printf("input array \n");
        for (i=0;i<=j;i++)
        {
        scanf("%d\n",&a[i]);
        }
        printf("this is your array \n");
        for (i=0;i<=j;i++)
        {
         printf("%d\n",a[i]);
        }
    return 0;
}

