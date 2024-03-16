#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
int main(int argc, char *argv[]) {
    int n = argc - 1;
    int arr[n];

    // Convert command line arguments to integers
    for (int i = 1; i < argc; i++) {
        arr[i - 1] =atoi(argv[i]);



    pid_t a=fork();
    if (a==0){
        arr[]={"./sort", NULL};
        execv(arr[0],args);
    }
    else{
        wait(NULL);
        arr[]={"./oddeven", NULL};
        execv(arr[0],argc);
    }
    return 0
}

}