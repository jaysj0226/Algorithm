#include <stdio.h>

void function(int n){
        int arr[n][n];

    int num=1;

    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            arr[j][i]=num;
            num++; 
        }
    }

    for(int i = 0; i<n; i++){
        for(int j=0; j<n; j++){
            printf("%d ",arr[i][j]);
        }
        printf("\n");
    }   
}

int main() {
    // Please write your code here.
    
    int n  = 2;
    scanf("%d",&n);

    function(n);
    return 0;
}
