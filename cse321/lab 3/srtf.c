#include <stdio.h>

int main(){

    int at[10],bt[10],rt[10],comptime,i,smallest;
    int remain=0,n,time,sumwait=0,sumtat=0;
    printf("Number of processes:");
    scanf("%d",&n);

    for (i=0;i<n;i++){
        printf("enter at of process P%d: ",i+1);
        scanf("%d",&at[i]);
        printf("enter bt of process P%d: ",i+1);
        scanf("%d",&bt[i]);
        rt[i]=bt[i];
    }
    printf("\n\nProcess\tTurnaaroundtime| wait time\n\n");
    for (time=0;remain!=n;time++){
        for(i=0;i<n;i++){
            if (at[i]<=time&& rt[i]){
                smallest=i;
            }
        }
        rt[smallest]--;
        if(rt[smallest]==0){
            remain++;
            comptime=time+1;
            printf("\nP[%d]\t|\t%d\t|\t%d", smallest+1,comptime-at[smallest],comptime-bt[smallest]-at[smallest]);
            sumwait=sumwait+comptime-bt[smallest]-at[smallest];
            sumtat=sumtat+comptime-at[smallest];
        }
    }
    printf("\n\nAverage wait time=%f\n",sumwait*1.0/n);
}