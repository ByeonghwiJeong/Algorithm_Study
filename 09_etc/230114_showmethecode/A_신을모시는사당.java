import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] dp = new int[3];
        int result = 0;
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(st.nextToken());
            dp[num]++;
            dp[num ^ 1 ^ 2] = Math.max(0, dp[num ^ 1 ^ 2] - 1);
            result = Math.max(result, dp[num]);
        }

        System.out.print(result);
    }
}