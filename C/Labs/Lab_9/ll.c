#include <stdio.h>
#include <stdlib.h>
#include "ll.h"

/* One of the lessons here is to see that if we want to use a function to malloc something that
 * is a POINTER in the CALLER of the function, then we must send in the ADDRESS of the POINTER
 * to that function.
 * 
 * Recap: if we want to use a function to modify a VARIABLE in the caller
 *        then the CALLER needs to send in the ADDRESS of the VARIABLE
 *
 * Similarly: if we want to use a function to modify a POINTER in the caller
 *            then the CALLER needs to send in the ADDRESS of the POINTER
 *
 * In the code below, ll_add_to_head and ll_add_to_tail are dynamically creating new
 * nodes to be added to the linked list. Any dynamic creation of a node must be via
 * malloc.
 */

int ll_add_to_head( llnode **head, int val) {
    llnode *old_head;
    if (head == NULL) {
        return -1;
    }
	old_head = *head;
    *head = ( llnode *) malloc(sizeof( llnode));
    (*head) -> val = val;
	(*head) -> next = old_head;
	return 0;
}

int ll_add_to_tail( llnode **head, int val) {
    if (head == NULL) {
        return -1;
    }
    if (*head == NULL) {
        *head = ( llnode *) malloc(sizeof( llnode));
        (*head) -> val = val;
        (*head) -> next = NULL;
        return 0;
    
    } else { /* recursively call ll_add_to_tail until we get to the tail
					which is the point where the pointer is NULL */
        return ll_add_to_tail(&((*head)->next), val);
   }
}

int ll_print( llnode *p) {
    if (p==NULL) {
        return 0;

    } else {
        printf("val = %d\n",p->val);
        return ll_print(p->next);
   }
}

int ll_free(llnode *p) {
    
    if (p==NULL) {
        return -1;

    } else {

        llnode *f=p->next;
        free(p);
        return ll_free(f);
   }
}

// New Code

int ll_find_by_value(llnode *pList, int val) {
    if (pList == NULL) {
        return -1;

    } else if (pList->val == val) {
        return 0;

    } else {

        return ll_find_by_value(pList->next, val);
    }
}

int ll_del_from_tail(llnode **ppList) {

    if (ppList == NULL) {
        return -1;

    } else if (*ppList == NULL) {
        return -1;

    } else if ((*ppList)->next == NULL) {
        free(*ppList);
        *ppList = NULL;
        return 0;

    } else if ((*ppList)->next->next == NULL) {
        free((*ppList)->next);
        (*ppList)->next = NULL;
        return 0;

    } else {
        return ll_del_from_tail(&((*ppList)->next));
    }
}

int ll_del_from_head(llnode **ppList) {

    if (ppList == NULL) {
        return -1;

    } else if (*ppList == NULL) {
        return -1;

    } else if ((*ppList)->next == NULL) {
        free(*ppList);
        *ppList = NULL;
        return 0;

    } else {
        llnode *old = *ppList;
        *ppList = old->next;
        free(old);
        return 0;
    }
}

/*

int ll_del_by_value(llnode **ppList, int val) {

    if (ppList == NULL) {
        return -1;

    } else if (*ppList == NULL) {
        return -1;// if done recursively cannot return if error or no error

    } else if ((*ppList)->val == val) {
        ll_del_from_head(ppList);
        return 0;
    
    } else if ((*ppList)->next != NULL) {
        
        return ll_del_by_value(&((*ppList)->next), val);

    } else {
        return -1;
    }
}

*/

int ll_del_by_value(llnode **ppList, int val) {
    llnode *current = *ppList;
    llnode *old = *ppList;

    if (ppList == NULL) {
        return -1;

    } else if ((*ppList)->val == val) {
        ll_del_from_head(ppList);
        //ll_del_by_value(ppList, val);
        return 0;

    } else if ((*ppList)->next == NULL) {
        if ((*ppList)->val == val) {
            free(*ppList);
            (*ppList) = NULL;
            return 0;

        } else {

            return -1;
        }
    } else {    
        
        current = (*ppList)->next;
        while (current != NULL) {
            if (current->val == val) {
                old->next = current->next;
                free(current);
                //ll_del_by_value(ppList, val);
                return 0;
            
            } else {

                old = current;
                current = current->next;
            }
        }
        return -1;
    }
}

int ll_concat(llnode **pSrcA,llnode **pSrcB) {
    if (pSrcA == NULL || pSrcB == NULL) {
        return -1;

    } else if (*pSrcA == NULL) {
        *pSrcA = *pSrcB;
        return 0;

    } else {

        llnode *old = *pSrcA;
        while (old->next != NULL) {
            old = old->next;
        }
        old->next = *pSrcB;
        return 0;
    }
}

int ll_insert_in_order(llnode **ppList, int val) {
    llnode *current, *old;

    if (ppList == NULL) {
        return -1;

    } else if (*ppList == NULL) {
        ll_add_to_tail(ppList, val);
        return 0;

    } else {

        current = *ppList;
        old = *ppList;
        while (current->next != NULL) {
            if (val >= current->val && val <= current->next->val) {

                old = (llnode *)malloc(sizeof(llnode));
                old->next = current->next;
                old->val = val;
                current->next = old;
                return 0;

            } else {
                current = current->next;
            }
        }
        
        if (current->val > val) {
            ll_add_to_head(ppList, val);

        } else {
            ll_add_to_tail(ppList, val);
        }
        return 0;
    }
}

int ll_sort(llnode **ppList) {
    llnode *temp;
    int test = 1;

     if (ppList == NULL) {
        return -1;

    } else if (*ppList == NULL) {
        return -1;

    } else if ((*ppList)->next == NULL) {
        return 0;

    } else {
        temp = *ppList;
        test = 1;
        while (test == 1) {
            test = 0;
            for (temp = *ppList; temp->next != NULL; temp = temp->next) {
                if (temp->val > temp->next->val) {
                    swapNodes(ppList, temp->val, temp->next->val);
                    test = 1;
                    break;
                }
            }
        }
        return 0;
    }
}

// Generic Algorithm to swapnodes to ease in sort above
int swapNodes(llnode **ppList, int nodeXval, int nodeYval) {
    llnode *oldX = NULL, *currentX = *ppList; // Variables for X
    llnode *oldY = NULL, *currentY = *ppList; // Variables for Y
    llnode *temp;

    // Search for X and keep track of oldX and currentX
    while (currentX && currentX->val != nodeXval) {

        oldX = currentX; 
        currentX = currentX->next; 
    } 
  
    // Search for Y and keep track of oldY and currentY
    while (currentY && currentY->val != nodeYval) { 

        oldY = currentY; 
        currentY = currentY->next;
    } 
  
    // Change if X is header or not
    if (oldX != NULL) {
        oldX->next = currentY; 

    } else {

        *ppList = currentY;
    }
  
    // Change if Y is header or not
    if (oldY != NULL) {
        oldY->next = currentX; 

    } else {

        *ppList = currentX; 
    }
  
    // Swap pointers 
    temp = currentY->next;
    currentY->next = currentX->next; 
    currentX->next = temp; 
    return 0;
}