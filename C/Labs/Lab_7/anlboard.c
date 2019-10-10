#include <stdio.h>

int analyzeBoard(int *, int);

int main(void) {
    int a[9] = {2,0,0,2,0,0,2,0,0};
    printf("%d", analyzeBoard(a, sizeof(a)/sizeof(int)));
    return 0;
}

int analyzeBoard(int *T, int sizeT) {
    if (sizeT == 9) {
        if (T[0] == T[1] && T[1] == T[2] && T[3] != 0) {
            return T[0];
                                
        } else if (T[3] == T[4] && T[4] == T[5] && T[5] != 0) {
            return T[3];
                        
        } else if (T[6] == T[7] && T[7] == T[8] && T[8] != 0) {
            return T[6];
                        
        } else if (T[0] == T[3] && T[3] == T[6] && T[6] != 0) {
            return T[0];
                        
        } else if (T[1] == T[4] && T[4] == T[7] && T[7] != 0) {
            return T[1];
                        
        } else if (T[2] == T[5] && T[5] == T[8] && T[8] != 0) {
            return T[2];
                        
        } else if (T[0] == T[4] && T[4] == T[8] && T[8] != 0) {
            return T[0];
                        
        } else if (T[2] == T[4] && T[4] == T[6] && T[6] != 0) {
            return T[2];
                        
        } else {
            if (T[0] == 0 || T[1] == 0 || T[2] == 0 || T[3] == 0 || T[4] == 0 || T[5] == 0 || T[6] == 0 || T[7] == 0 || T[8] == 0) {   
                return 0;
                        
            } else {
                return 3;
            }
        }
    }
    return -1;
}