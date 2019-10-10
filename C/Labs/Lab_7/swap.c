#include<stdio.h>

int swap(int *, int *);

int main(void) {
  int a = 0, b = 0;
  scanf("%d", &a);
  scanf("%d", &b);
  swap(&a, &b);
  printf("%d\n", a);
  printf("%d\n", b);
}

int swap (int *a, int *b) {
  int x = *a;
  *a = *b;
  *b = x;
  return 1;
}