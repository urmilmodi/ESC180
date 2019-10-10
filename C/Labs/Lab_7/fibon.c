#include <stdio.h>

int fibo(int n);

int main(void) {
   int i = 0, d = 0;
   scanf("%d", &d);
   for (i=0;i<d;i=i+1){
      int f = fibo(i);
      printf("fibo(%d)=%d\n",i,f);
   }

   return 0;
}

int fibo(int n){
   if (n == 0 || n == 1) {
     
     return 1;
   } else if (n > 0) {

     return fibo(n - 1) + fibo(n - 2);
   }
}