#include <stdio.h>

void function(int n, int m){
    int arr[n][m];
    int num = 1;


    for(int d=0; d <= (n+m)-2; d++){
        for(int i=0; i<n; i++){
            int j = d-i;
            if(j >= 0 && j < m){
                arr[i][j] = num;
                num++;
            }
        }
    }

    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            printf("%d ", arr[i][j]);
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