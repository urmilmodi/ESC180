#include<stdio.h>
#include<stdlib.h>

int fill(float* matrixIn, int rows, int cols, float ** matrixOut);

int fill(float* matrixIn, int rows, int cols, float ** matrixOut) {
    int i = 0, j = 0;
    if (matrixIn == NULL || rows < 1 || cols < 1 || matrixOut == NULL) {return -1;}

    while (*matrixOut == NULL) {
        *matrixOut = (float *)malloc(sizeof(float)*rows*cols);
    }

    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {
            if (matrixIn[i*cols + j] < 0) {
                (*matrixOut)[i*cols + j] = 0;

            } else {
                (*matrixOut)[i*cols + j] = matrixIn[i*cols + j];
            }
        }
    }
    return 0;
}