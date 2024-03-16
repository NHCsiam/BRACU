#include <stdio.h>
#include <stdbool.h>

#define num_of_processes 5
#define num_of_resources 4

int available[num_of_resources];
int allocation[num_of_processes][num_of_resources];
int max[num_of_processes][num_of_resources];
int need[num_of_processes][num_of_resources];

void initialize() {
    int i, j;
    //  available resources
    int available[num_of_resources]= { 3, 3, 2, 1 };

    //  allocation matrix
    int allocation[num_of_processes][num_of_resources]= { { 0, 1, 0, 3 }, { 2, 0, 0, 0 },{ 3, 0, 2, 0 }, { 2, 1, 1, 5 },{ 0, 0, 2, 2 } };

    //  max matrix
    int max[num_of_processes][num_of_resources]={ { 6, 4, 3, 4 },{ 3, 2, 2, 1 },{ 9, 1, 2, 6 },{ 2, 2, 2, 8 },{ 4, 3, 3, 7 } };

    // need matrix
    for (i = 0; i < num_of_processes; i++) {
        for (j = 0; j < num_of_resources; j++) {
            need[i][j] = max[i][j] - allocation[i][j];
        }
    }
}

bool safe() {
    int i, j, k;
    int work[num_of_resources];
    bool finish[num_of_processes];

    for (i = 0; i < num_of_resources; i++) {
        work[i] = available[i];
    }

    for (i = 0; i < num_of_processes; i++) {
        finish[i] = false;
    }
    for (i = 0; i < num_of_processes; i++) {
        for (j = 0; j < num_of_processes; j++) {
            if (!finish[j]) {
                bool canExecute = true;
                for (k = 0; k < num_of_resources; k++) {
                    if (need[j][k] > work[k]) {
                        canExecute = false;
                        break;
                    }
                }

                if (canExecute) {
                    for (k = 0; k < num_of_resources; k++) {
                        work[k] += allocation[j][k];
                    }
                    finish[j] = true;
                }
            }
        }
    }
    for (i = 0; i < num_of_processes; i++) {
        if (!finish[i]) {
            return false;
        }
    }

    return true;
}

int main() {
    initialize();
    if (safe()) {
        printf("Safe here\n");
    } else {
        printf("Deadlock Ahead\n");
    }
    return 0;
}
