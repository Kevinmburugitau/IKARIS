# include <stdio.h>

int main(){
    int a;
    printf("Enter marks \n");
    scanf("%d",&a);
    if (a>100)
    {
        printf("invallid\n");
    }
    else if (a>=70)
    {
        printf("A\n");
    }
    else if (a>=60)
    {
        printf("B\n");
    }
    else if (a>=50)
    {
        printf("C\n");
    }
    else if (a>=40)
    {
        printf("D\n");
    }
    else{
        printf("Fail \n");
    }
    
  return 0;  
}