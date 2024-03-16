#include <stdio.h>
#include <stdbool.h>

#define num_of_processes 6
#define num_of_resources 4

int available[num_of_resources];
int allocation[num_of_processes][num_of_resources];
int max[num_of_processes][num_of_resources];
int need[num_of_processes][num_of_resources];

void initialize() {
    int i, j;
    //  available resources
    available[0] = 2;
    available[1] = 2;
    available[2] = 2;
    available[3] = 1;

    //  allocation matrix
    int alloc[num_of_processes][num_of_resources]= { { 0, 1, 0, 3 }, { 2, 0, 0, 3 },{ 3, 0, 2, 0 }, { 2, 1, 1, 5 }, { 0, 0, 2, 2 }, { 1, 2 , 3, 1 } };
    for (i = 0; i < num_of_processes; i++) {
        for (j = 0; j < num_of_resources; j++) {
            allocation[i][j] = alloc[i][j];
        }
    }

    //  max matrix
    int maximum[num_of_processes][num_of_resources]= { { 6, 4, 3, 4 }, { 3, 2, 2, 4 },{ 9, 1, 2, 6 }, { 2, 2, 2, 8 }, { 4, 3, 3, 7 }, { 6, 2 , 6, 5 } };
    for (i = 0; i < num_of_processes; i++) {
        for (j = 0; j < num_of_resources; j++) {
            max[i][j] = maximum[i][j];
        }
    }

    // need matrix
    for (i = 0; i < num_of_processes; i++) {
        for (j = 0; j < num_of_resources; j++) {
            need[i][j] = max[i][j] - allocation[i][j];
        }
    }
}

bool safe(int* sequence) {
    int i, j, k;
    int work[num_of_resources];
    bool finish[num_of_processes];

    for (i = 0; i < num_of_resources; i++) {
        work[i] = available[i];
    }

    for (i = 0; i < num_of_processes; i++) {
        finish[i] = false;
    }

    int count = 0;
    while (count < num_of_processes) {
        bool found = false;
        for (i = 0; i < num_of_processes; i++) {
            if (!finish[i]) {
                bool canExecute = true;
                for (k = 0; k < num_of_resources; k++) {
                    if (need[i][k] > work[k]) {
                        canExecute = false;
                        break;
                    }
                }

                if (canExecute) {
                    for (k = 0; k < num_of_resources; k++) {
                        work[k] += allocation[i][k];
                    }
                    finish[i] = true;
                    sequence[count] = i;
                    count++;
                    found = true;
                }
            }
        }
        if (!found) {
            return false; // Deadlock
        }
    }

    return true; // Safe sequence
}

int main() {
    initialize();
    int sequence[num_of_processes];
    if (safe(sequence)) {
        printf("Safe sequence: ");
        for (int i = 0; i < num_of_processes - 1; i++) {
            printf("P%d -> ", sequence[i]);
        }
        printf("P%d\n", sequence[num_of_processes - 1]);
    } else {
        printf("Deadlock Ahead\n");
    }
    return 0;
}