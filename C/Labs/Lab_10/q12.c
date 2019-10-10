#include<stdio.h>
#include<stdlib.h>

typedef struct {
    int valid, value, frequency;
} w;

int histogram(int* n, w** m, int s) {
    int i = 0, j = 0, accum = 0;
    if (n == NULL || s<1|| m == NULL) {return -1;}

    for (i = 0; i < s; i++) {
        for (j = 0; j < s; j++) {
            if(n[i] == m[i]->value) {
                accum++;
            }
        m[i]->frequency = accum;
        }
    }
    return 0;
}