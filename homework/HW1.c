/* 

Author: Dane Magbuhos
Date: 09/10/18
Course: CMSC 331

*/


#include <stdio.h>
#include <stdlib.h>

// Function populates array
int *getArray(int size){

  int *array_to_return;
  int multiplier = 2;
  int i = 0;
  
  // Creates dynamic array
  array_to_return = malloc(size * sizeof(*array_to_return));


  // Populates array with values
  for (i = 0; i < size; ++i){
    array_to_return[i] = i*multiplier;
  }

  return array_to_return;

}



int main(){

  int *returnedArray;
  int size = 10;
  int j = 0;

  // Calls getArray and returns populated array
  returnedArray = getArray(size);

  // Outputs array contents
  for (j = 0; j < size; j++){
    printf("returnedArray[%d] = %d\n" , j, returnedArray[j]);
  }

  // Frees up memory before exiting to prevent memory leaks
  free(returnedArray);

  return 0;

}
