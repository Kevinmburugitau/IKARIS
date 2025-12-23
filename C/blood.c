# include <stdio.h>
# include <ctype.h>
int main(){
  char blood;
  blood = toupper(blood);
  blood = tolower(blood);
  printf("enter your blood group(A,B,O,AB):");
  scanf("%c\n" , &blood);
  switch (blood)
  {
  case 'A':printf("DONATE TO AB A RECEIVE O AB");break;
  case 'B':printf("DONATE TO AB B RECEIVE O AB");break;
  case 'O':printf("UNVERSAL DONOR RECEIVE O");break;
  default:printf("DONATE TO A B AB UNIVERSAL RECEIVER");break;
  }//comment
