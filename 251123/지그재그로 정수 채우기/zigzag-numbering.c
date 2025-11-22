#include <stdio.h>

void function(int n, int m){

    int arr[n][m];
    int num = 0;

    for(int i=0; i<m; i++){
        if(i % 2 != 0 ){
            for(int j=n-1; j >=0; j--){
                arr[j][i] = num;
                num++;
            }
        }
        else{
            for(int j=0; j<n; j++){
                arr[j][i] = num;
                num++;
            }
        }
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j<m; j++){
            printf("%d ",arr[i][j]);
        }
        printf("\n");
    }

}

int main() {
    // Please write your code here.
    int n,m;
    scanf("%d %d", &n,&m);

    function(n,m);
    return 0;
}