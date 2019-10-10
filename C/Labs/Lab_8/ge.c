#include<stdio.h>
#include<stdlib.h>

int ge_fw(float *matrix, int rows, int cols, float *matrix_out);
int ge_bw(float *matrix, int rows, int cols, float *matrix_out);

int ge_fw(float *matrix, int rows, int cols, float *matrix_out) {

    if (matrix == NULL || rows == 0 || cols == 0 || matrix_out == NULL) {
        return -1;
    }

    int v = rows;
    if (rows > cols) {
        v = cols;
    }

    int k = 0;
    for (k = 0; k < v; k++) {

        // Interchange 1st Row
        int i = k;
        for (i = k; i < rows; i++) { // Go through all rows
            if (matrix[i*cols + k] != 0) { // For each non-zero col
                
                float x[cols];
                int j = 0;
                for (j = 0; j < cols; j++) {
                    x[j] = matrix[k*cols + j];
                }

                for (j = 0; j < cols; j++) {
                    matrix[k*cols + j] = matrix[i*cols + j];
                }

                for (j = 0; j < cols; j++) {
                    matrix[i*cols + j] = x[j];
                }
                
                break; // Once array is found stop
            }
        }
        float x = 0;
        i = k + 1;
        for (i = k + 1; i < rows; i++) {
            
            if (matrix[i*cols + k] != 0) {
                x = matrix[i*cols + k] / matrix[k*cols + k];
                
                int j = 0;
                for (j = 0; j < cols; j++) {
                    matrix[i*cols + j] -= x*matrix[k*cols + j];
                }
            }
        }
    }
    
    int i = 0, j = 0;
    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {
            if (matrix[i*cols + j] == -0.000) {
                matrix[i*cols + j] = 0.000;
            }
            matrix_out[i*cols + j] = matrix[i*cols + j];
        }
    }
    return 0;
}

int ge_bw(float *matrix, int rows, int cols, float *matrix_out) {

    if (matrix == NULL || rows == 0 || cols == 0 || matrix_out == NULL) {
        return -1;
    }

    int v = rows;
    if (rows > cols) {
        v = cols;
    }

    int k = v, n = -1, j = k, i = k;
    float x = 0;
    for (k = v - 1; k > -1; k--) {
        n = -1, j = k;
        
        for (j = k; j > -1; j--) {

            if (matrix[k*cols + j] != 0) {
                x = matrix[k*cols + j];
                n = j;
                i = 0;
                for (i = 0; i < cols; i++) {
                    matrix[k*cols + i] = matrix[k*cols + i] / x;
                }

                break;
            }
        }

        if (n != -1) {
            for (i = 0; i < rows; i++) {
                    if (i != k && matrix[i*cols + n] != 0) {
                        x = matrix[i*cols + n];
                        j = 0;
                        for (j = 0; j < cols; j++) {
                            matrix[i*cols + j] = matrix[i*cols + j] - x*matrix[k*cols + j];
    
                        }
                    }
                }
        }
    }

    i = 0, j = 0;
    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {
            if (matrix[i*cols + j] == -0.000) {
                matrix[i*cols + j] = 0.000;
            }
            matrix_out[i*cols + j] = matrix[i*cols + j];
        }
    }
    return 0;
}
