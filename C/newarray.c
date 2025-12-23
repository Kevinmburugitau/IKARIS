#include <stdio.h>

int main(void) {
    int i, j;
    printf("input size of the array: ");
    if (scanf("%d", &j) != 1 || j <= 0) {
        printf("Invalid size\n");
        return 1;
    }

    int a[j];           // now 'a' has the right size
    printf("input array:\n");
    for (i = 0; i < j; i++) {
        scanf("%d", &a[i]);   // drop the '\n'
    }

    printf("your array:\n");
    for (i = 0; i < j; i++) {
        printf("%d\n", a[i]);
    }

    return 0;
}
