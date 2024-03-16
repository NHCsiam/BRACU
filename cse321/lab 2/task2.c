#include <stdio.h>

int perfect(int start, int end){

    int i,n;
    for(start;start<=end;start++){
        int sum=0;
        for(i=1;i<start;i++){
            if (start%i==0){
                sum+=i;
            }
        }
        if (sum==start){
            printf("%d\n",sum);
        }
    }
}

int main(){

    int start;
    int end;
    printf("");
    scanf("%d", &start);
    printf("");
    scanf("%d",&end);
    perfect(start,end);
}


