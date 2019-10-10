#include<stdio.h>

int isPrime(int n) {
    int i  = 0;
    if (n < 2) {return -1;}
    for (i = 0; i < n; i++) {
        if (n%i == 0) {return -1;}
    }
    return 0;
}

int isPrimeProduct(int n) {
    int i = 0, j = 0;
    if (n < 1) {return -1;}
    if (isPrime(n) == 0) {return -1;}

    for (i = 0; i <n; i++) {
        if(isPrime(i) == 0 && n%i == 0) {
            for (j = 0; j < n/i; j++) {
                if(isPrime(j) == 0 && (n/i)%j == 0) {
                    return 0;
            }
        }
    }
    return -1;
}