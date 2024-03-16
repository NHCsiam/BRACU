#include <stdio.h>
#include <pthread.h>

#define NUM_THREADS 5

void *printThreadID(void *threadID) {
    printf("Thread %ld is running.\n", (long) threadID);
    pthread_exit(NULL);
}

int main() {
    pthread_t threads[NUM_THREADS];
    int rc, t;

    for (t = 0; t < NUM_THREADS; t++) {
        printf("Creating thread %d\n", t);
        rc = pthread_create(&threads[t], NULL, printThreadID, (void *) t);

        pthread_join(threads[t], NULL);
        printf("Thread %d has completed.\n", t);
    }

    pthread_exit(NULL);
}
