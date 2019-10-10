#include<stdio.h>
#include<stdlib.h>

typedef struct {
    int valid, value, frequency;
} w;

int getmode(w** m, int* mode, int s) {
    int i = 0, a = 0;
    if (m == NULL || mode == NULL || s < 1) {return -1;}
    for (i = 0; i < s; i++) {
        if (m[i]->frequency > a) {
            a = m[i]->frequency;
        }
    }
    *mode = a;
}