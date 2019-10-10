#include<stdio.h>
#include<stdlib.h>

int nsum(float* a, float* b, int n, float ** output);

int main(void) {
    printf("a and b should be float arrays");
    printf("n is an int, it is the size of a and b");
    printf("output will be of type float**");
}

int nsum(float* a, float* b, int n, float ** output) {
    int i = 0;
    if (a == NULL || b ==  NULL || n < 1 || output == NULL || *output == NULL) {
        return -1;
    }

    (*output) = (float*)malloc(sizeof(float)*n);
    for (i = 0; i < n; i++) {
        (*output)[i] = a[i] + b[i];
    }
    return 0;
}