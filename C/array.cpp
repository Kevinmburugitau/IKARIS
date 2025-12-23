#include <stdio.h>
int main (){
    int i;
    int j;
    
         printf("input size of the array \n");
         scanf("%d",&i);
        printf("input array \n"); 
        int a[i]={};
    for (i=0;i<j;i++)
    {
        scanf("%d\n",&a[i]);
    }
    printf("yor array\n");
    for (i=0;i<j;i++)       
    {
        printf("%d\n",a[i]);
    }
  
    for(int i = 0; i < j -1; i++) {
        int smallestPos = i;
        for( int k = i +1; k < j; k++) {
            if ( a[k] < a[smallestPos]) {
                smallestPos = k;
            }
        }
        int temp = a[i];
        a[i] = a[smallestPos];
        a[smallestPos] = temp;
    }
    printf("After sorting: ");
    for(int i = 0; i < j; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");
   


    return 0;
}