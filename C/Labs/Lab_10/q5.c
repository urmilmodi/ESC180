#include<stdio.h>
#include<stdlib.h>

int f(void);
int g(char**, int);

int f (void) {
    char* c = NULL;
    int x = 5;
    g(&c, x);
    return 0;
}

int g(char** c, int x) {
    *c = (char*)malloc(sizeof(char)*x);
    if (*c == NULL) {return -1;}
    else {return 0;}
}