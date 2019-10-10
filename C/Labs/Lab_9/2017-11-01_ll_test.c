#include <stdio.h>
#include "ll.c"

int main(void) {
   llnode *root = NULL;
   int r=0;
   int i=0;

   printf("List A\n");
   r=ll_add_to_tail(&root,100);
   r=ll_add_to_tail(&root,200);
   r=ll_add_to_tail(&root,300);
   for(i=0;i<10;i=i+1){
      r=ll_add_to_tail(&root,i*100);
   }
   r=ll_print(root);
   r=ll_free(root);

   printf("List B\n");
	root=NULL;
   r=ll_add_to_tail(&root,100);
   r=ll_add_to_tail(&root,200);
   r=ll_add_to_tail(&root,300);
   r=ll_print(root);
   printf("k\n");
   ll_sort(&root);
   r=ll_print(root);
   r=ll_free(root);
   return 0;
}
