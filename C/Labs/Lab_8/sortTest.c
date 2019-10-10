#include<stdio.h>
#include<stdlib.h>
#include "sort.c"

int main(void) {

    int x[] = {4,4,4,4,4,4,5,4,5,5,46,4,564,5,45,45,1,546,5,-8,-9,-456545,-4564,-1};
    printf("%d\n", bubbleSort(x, sizeof(x)/sizeof(int)));

    int y[] = {4,4,4,4,4,4,4,4,4,4,4,4};
    printf("%d\n", bubbleSort(y, sizeof(y)/sizeof(int)));

   // int z[] = {};
    //printf("%d", bubbleSort(z, sizeof(z)/sizeof(int)));

    return 0;
}