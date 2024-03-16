#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main(){
    int count=1;
    pid_t a,b,c;
    a=fork();
    if (a==0){
        if (getpid%2!=0){
            b=fork();
            // count++;
            if (b==0){
                if (getpid%2!=0){
                    c=fork();
                    // count++;
                    if (c==0){
                        if (getpid%2!=0){
                            count++;
                        }
                    }else{
                        wait(NULL);
                    }
                }count++;
            }else{
                wait(NULL);
            }
        count++;
        }
    }else{
        wait(NULL);
    }
    printf("total process number: %d", count);
    return 0;
}

