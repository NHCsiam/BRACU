#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

void grandchild() {
    printf("I am grandchild\n");
}

void child() {
    printf("I am child\n");
    pid_t pid = fork();
    if (pid == 0) {
        grandchild();
    } else {
        wait(NULL);
    }
}

int main() {
    printf("I am parent\n");
    pid_t pid = fork();
    if (pid == 0) {
        child();
    } else {
        wait(NULL);
    }
    return 0;
}
