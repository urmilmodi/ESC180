#include <stdio.h>

int analyzeBoard(char *, int);
int convert(char);

int main(void) {
    char a[9] = {'X','-','-','X','-','-','X','-','-'};
    printf("%d", analyzeBoard(a, sizeof(a)/sizeof(char)));
    return 0;
}

int analyzeBoard(char *T, int sizeT) {
    if (sizeT == 9) {
        if (T[0] == T[1] && T[1] == T[2] && T[2] != '-') {
            return convert(T[0]);
                                
        } else if (T[3] == T[4] && T[4] == T[5] && T[5] != '-') {
            return convert(T[3]);
                        
        } else if (T[6] == T[7] && T[7] == T[8] && T[8] != '-') {
            return convert(T[6]);
                        
        } else if (T[0] == T[3] && T[3] == T[6] && T[6] != '-') {
            return convert(T[0]);
                        
        } else if (T[1] == T[4] && T[4] == T[7] && T[7] != '-') {
            return convert(T[1]);
                        
        } else if (T[2] == T[5] && T[5] == T[8] && T[8] != '-') {
            return convert(T[2]);
                        
        } else if (T[0] == T[4] && T[4] == T[8] && T[8] != '-') {
            return convert(T[0]);
                        
        } else if (T[2] == T[4] && T[4] == T[6] && T[6] != '-') {
            return convert(T[2]);
                        
        } else {
            if (T[0] == '-' || T[1] == '-' || T[2] == '-' || T[3] == '-' || T[4] == '-' || T[5] == '-' || T[6] == '-' || T[7] == '-' || T[8] == '-') {   
                return 0;
                        
            } else {
                return 3;
            }
        }
    }
    return -1;
}

int convert(char a) {
    if (a == 'X') {
        return 1;

    } else {
        return 2;
    }
}