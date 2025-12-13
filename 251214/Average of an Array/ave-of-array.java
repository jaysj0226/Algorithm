import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[][] arr = new int[2][4];

        // 입력
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 4; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        // 1) 행 평균
        for (int i = 0; i < 2; i++) {
            int sum = 0;
            for (int j = 0; j < 4; j++) sum += arr[i][j];
            double avg = sum / 4.0;
            System.out.printf("%.1f ", avg);
        }

        System.out.println();

        // 2) 열 평균
        for (int i = 0; i < 4; i++) {
            int sum = 0;
            for (int j = 0; j < 2; j++) sum += arr[j][i];
            double avg = sum / 2.0;
            System.out.printf("%.1f ", avg);
        }

        System.out.println();

        // 3) 전체 평균
        int total = 0;
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 4; j++) total += arr[i][j];
        }
        double totalAvg = total / 8.0;
        System.out.printf("%.1f", totalAvg);
    }
}
