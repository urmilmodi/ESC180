#include<stdio.h>

struct poly {
    float coefficient, power;
    struct poly* next;
};
typedef struct poly poly;

int integrate(poly**);

int integrate(poly** x) {
    poly* y = *x;
    if (x == NULL) {return -1;}
    if (*x == NULL) {return -1;}    

    while (y->next != NULL) {

        y->coefficient = y->coefficient/(y->power + 1);
        y->power++;
        y = y->next;
    }
    y->coefficient = y->coefficient/(y->power + 1);
    y->power++;
    return 0;
}