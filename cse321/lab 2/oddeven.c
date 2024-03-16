#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    
    for (int i=1; i<argc;i++){
        int j=atoi(argv[i]);
        if (j%2==0){
            printf("%d is even\n",j);
        }else{
            printf("%d is odd\n",j);
        }
    }
    return 0;
}



















