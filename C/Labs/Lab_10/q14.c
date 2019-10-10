#include<stdio.h>
#include<stdlib.h>

int fibo(int n) {
    if (n < 0) {return -1;}
    if (n == 0 || n == 1 || n == 2) {return 1;}
    else {
        return fibo(n-1) + fibo(n-2) + fibo(n-3);
    }
}