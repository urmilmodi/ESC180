#include <stdio.h>

int fibi(int);
int fibr(int);
int fibarray(int);
int printfibarray(int);

int main(void) {
    int N;
    printf("Enter Number of Fibonancci Number Desired: ");
    scanf("%d", &N);
    printfibarray(N);
    return 0;
}

int fibi(int N) {
    if (N == 0 || N == 1) {
        return 1;
    }
    else if (N > 0) {
        int v[N];
        v[0] = 1;
        v[1] = 1;
        for (int i = 0; i < N - 2; i++) {
            v[i + 2] = v[i] + v[i + 1];
        }
        return v[N - 1];
    }
}

int fibr(int N) {
    if (N == 0 || N== 1) {
        return 1;

    } else {
        return fibr(N - 1) + fibr ( N - 2);
    }
}

int fibarray(int N) {
    int data[N];
    for (int i = 0; i < N; i++) {
        data[i] = fibr(i);
    }
    return 0;
}

int printfibarray(int N) {
    int data[N];
    for (int i = 0; i < N; i++) {
        data[i] = fibr(i);
    }
    for (int i = 0; i < N; i++) {
        printf("%d\n", data[i]);
    }
    return 0;
}