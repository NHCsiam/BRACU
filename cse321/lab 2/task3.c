#include <stdio.h>
#include<string.h>
#include <fcntl.h>

int main(){

    int output;
    char a[100];
    output=open("output.txt",O_RDWR| O_CREAT);
    printf("Enter a string: ");
    fgets(a,100,stdin);


    while (strcmp(a,"-1\n")==0)
    {
        printf("Enter a string: ");
        fgets(a,100,stdin);
    }
    write(output,a,strlen(a));
    close(output);
}