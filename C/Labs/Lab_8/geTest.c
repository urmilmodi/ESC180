#include<stdio.h>
#include<stdlib.h>
#include "ge.c"

int printMatrix(float*, int, int);

int main(void) {
    
    int rows = 5, cols = 3;
    float x[5][3] = {{1,2,3}, {4,5,6}, {7,8,9}, {10,11,12}, {13,14,15}};
    float y[5][3] = {{1,2,3}, {4,5,6}, {7,8,9}, {10,11,12}, {13,14,15}};

    ge_fw(&x[0][0], rows, cols, &y[0][0]);
    //printMatrix((float *)y, rows, cols);
    ge_bw(&x[0][0], rows, cols, &y[0][0]);
    printMatrix((float *)y, rows, cols);

    rows = 3, cols = 3;
    float a[3][3] = {{1,2,3}, {4,5,6}, {7,8,9}};
    float b[3][3] = {{1,2,3}, {4,5,6}, {7,8,9}};

    ge_fw(&a[0][0], rows, cols, &b[0][0]);
    //printMatrix((float *)b, rows, cols);
    ge_bw(&a[0][0], rows, cols, &b[0][0]);
    printMatrix((float *)b, rows, cols);
    
    rows = 3, cols = 5;
    float c[3][5] = {{1,2,3,4,5}, {6,7,8,9,10}, {11,12,13,14,15}};
    float d[3][5] = {{1,2,3,4,5}, {6,7,8,9,10}, {11,12,13,14,15}};

    ge_fw(&c[0][0], rows, cols, &d[0][0]);
   // printMatrix((float *)d, rows, cols);
    ge_bw(&c[0][0], rows, cols, &d[0][0]);
    printMatrix((float *)d, rows, cols);

    return 0;
}

int printMatrix(float *x, int rows, int cols) {
    
    int i = 0, j = 0;
    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {
            printf("%8.3f", x[i*cols + j]);
        }
        printf("\n");
    }
    printf("-----------------\n");
    return 0;
}