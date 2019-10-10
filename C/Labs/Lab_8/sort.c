#include<stdio.h>
#include<stdlib.h>

int bubbleSort(int *x, int size);

int bubbleSort(int *x, int size) {
    if (x == NULL || size == 0) {
        return -1;

    } else {

        int swap = 1, y = 0;
        while (swap) {
            swap = 0;
            int i = 0;
            for(i = 1; i < size; i++) {
                if (x[i - 1] > x[i]) {
                    y = x[i];
                    x[i] = x[i - 1];
                    x[i - 1] = y;
                    swap = 1;
                    break;
                }
            }
        }
        return 0;
    }
}