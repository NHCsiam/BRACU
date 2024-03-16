#include <stdio.h>

int main() {
    int burst_time[100], waiting_time[100], turnaround_time[100];
    int n, quantum, i, j, time, remaining;
    printf("Enter the number of processes: ");
    scanf("%d", &n);
    printf("Enter burst time for each process:\n");
    for (i = 0; i < n; i++) {
        scanf("%d", &burst_time[i]);
    }
    printf("Enter time quantum: ");
    scanf("%d", &quantum);
    remaining = n;
    time = 0;
    for (i = 0; i < n; i++) {
        waiting_time[i] = 0;
    }
    printf("\nGantt Chart:\n");
    printf("\n");
    printf("| ");
    while (remaining > 0) {
        for (i = 0; i < n; i++) {
            if (burst_time[i] > 0) {
                if (burst_time[i] > quantum) {
                    time += quantum;
                    burst_time[i] -= quantum;
                    printf("P%d | ", i+1);
                } else {
                    time += burst_time[i];
                    waiting_time[i] = time - burst_time[i];
                    turnaround_time[i] = time;
                    burst_time[i] = 0;
                    remaining--;
                    printf("P%d | ", i+1);
                }
            }
        }
    }
    printf("\n \n");
    float total_waiting_time = 0, total_turnaround_time = 0;
    for (i = 0; i < n; i++) {
        total_waiting_time += waiting_time[i];
        total_turnaround_time += turnaround_time[i];
        printf("Process %d: waiting time = %d, turnaround time = %d\n", i+1, waiting_time[i], turnaround_time[i]);
    }
    printf("Average waiting time = %f\n", total_waiting_time / n);
    printf("Average turnaround time = %f\n", total_turnaround_time / n);
    
    return 0;
}
