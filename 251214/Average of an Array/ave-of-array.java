import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int[][] arr = new int[2][4];

        for(int i=0; i<2; i++)
        {
            for(int j=0; j<4; j++)
            {
                arr[i][j] = sc.nextInt();
            }
        }
        for(int i=0; i<2; i++)
        {
            int sum=0;
            float ans=0;
            for(int j=0; j<4; j++)
            {
                
                sum += arr[i][j];   
                ans = sum / 4;
            }
            System.out.print(ans+" ");
            
        }
        System.out.println();
        for(int i=0; i<4; i++)
        {
            int sum=0;
            float ans=0;
            for(int j=0; j<2; j++)
            {
                sum += arr[j][i];
                ans = sum/2;
            }
            System.out.print(ans+" ");
        }
        int sum=0;
        float ans=0;
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<2; j++)
            {
                sum += arr[j][i];
            }
        }
        ans = sum/8;
        System.out.println();
        System.out.print(ans);
    }
}