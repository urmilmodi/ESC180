#include<stdio.h>
#include<stdlib.h>

int printMatrix(float*, int, int);
/*
int main(void) {
    int rows = 0, cols = 0;
    while (rows == 0 || rows < 0) {
        printf("Rows: ");
        scanf("%d", &rows);
    }
    
    while (cols == 0 || cols < 0) {
        printf("Cols: ");
        scanf("%d", &cols);
    }

    float *x = NULL;
    while (x == NULL) {
        x = (float *)malloc(rows*cols*sizeof(float));
    }

    int i = 0, j = 0;
    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {

            x[i*cols + j] = j;
        }
    }

    int r = printMatrix((float *)x, rows, cols);
    if (r != 0)  {
        return -1;
    }
    return 0;
}
*/
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