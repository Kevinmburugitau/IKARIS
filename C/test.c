#include <stdio.h>
    union test
    {
        int ID;
        int age;
        char name[20];
        float height;
    }; 
 int main (){
    union test s;
    scanf("%d",&s.ID);
    scanf("%d",&s.age);
    scanf("%s",s.name);
    scanf("%2f",&s.height);
    printf("%d",s.ID);
    printf("%d",s.age);
    printf("%s",s.name);
    printf("%2f",s.height);
    return 0;
}