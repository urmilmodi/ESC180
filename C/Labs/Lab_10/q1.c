#include<stdio.h>

float avg(float * x, int size) {
    int i = 0;
    float y = 0;
    if (x == NULL) {return -1;}
    if (size < 1) {return -1;}

    for (i = 0; i < size; i++) {
        y += x[i];
    }
    return y;
}