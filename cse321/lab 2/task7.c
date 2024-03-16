#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(){

    pid_t child, granc1,granc2,granc3;
    printf("1.Parent process ID: %d\n",getpid());
    wait(NULL);
    child=fork();
    if (child==0){
        printf("2.Child process ID: %d\n",getpid());
        granc1=fork();
        if (granc1==0){
            printf("3.first grandchild process ID: %d\n", getpid());
            granc2=fork();
            if (granc2==0){
                printf("4.second grandchild process ID: %d\n", getpid());
                granc3=fork();
                if (granc3==0){
                    printf("5.third grandchild process ID: %d\n", getpid());
                }
            }
        }   
    }
    return 0;
}
















        // }if (granc2==0){
        //         printf("second grandchild process ID: %d\n", getpid());
        //     }else{
        //         granc3=fork();
        //         if (granc3==0){
        //             printf("third grandchild process ID: %d\n", getpid());
        //         }

        //     }