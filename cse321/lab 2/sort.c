#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int arr[argc-1]; // Declare an array of size argc-1
    int n = argc - 1; // Set the number of elements in the array
    int i, j, temp;


    // printf("The elements in the array are: ");
    for(int i = 1; i < argc; i++) {
      arr[i-1] = atoi(argv[i]); // Convert each command line argument to integer and store it in the array
    //   printf("%d ", arr[i-1]); // Print each element in the array
    }
    for (i = 0; i < argc - 2; i++) {
        for (j = 0; j < argc - i - 2; j++) {
            if (arr[j] < arr[j+1]) {
            temp = arr[j];
            arr[j] = arr[j+1];
            arr[j+1] = temp;
            }
        }
    }
    printf("Sorted Array in descending order: ");
    for (i = 0; i < argc - 1; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;

}
























