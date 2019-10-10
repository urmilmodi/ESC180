#include <stdio.h>

float myabs(float);
float bsqrt(float, float);

int main(void) {
    float x;
    printf("\nSqrt of: ");
    scanf("%f", &x);
    float error;
    printf("Error: ");
    scanf("%f", &error);
    float sqrtx = bsqrt(x, error);
    printf("%f", sqrtx);
    return 0;
}

float bsqrt(float x, float error) {
    float esti = x/2;
    while (myabs(esti*esti - x) >= error) {
        esti = (esti + x/esti)/2;
    }
    return esti;
}

float myabs(float x) {
    if (x < 0) {
        return -x;
    }
    return x;
}