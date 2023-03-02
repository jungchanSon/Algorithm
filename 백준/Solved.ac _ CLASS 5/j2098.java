import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;
public class Main {
    static int n;
    static int[][] graph;
    static int[][] dp;
    static int INF = 100000000;

    
    private static int dfs(int start, int visited){
        
        if (visited == (1 << n) - 1) {
            if (graph[start][0] != 0){
                return graph[start][0];
            }else{
                return INF;
            }
        }

        if (dp[start][visited] != INF) {
            return dp[start][visited];
        }

        for(int i=0; i<n; i++) {
            if ((visited & (1 << i)) != 0 || graph[start][i] == 0){
                continue;
            }

            dp[start][visited] = Math.min(dp[start][visited], dfs(i, visited | (1<<i)) + graph[start][i]);
        }
        
        return dp[start][visited];
    }
    
    public static void main(String args[]) throws IOException, NumberFormatException{
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
        n = Integer.valueOf(br.readLine());
        graph = new int[n][n];
        dp = new int[n][(1<<n) - 1];

        StringTokenizer st;
        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < n; j++) {
                int weight = Integer.valueOf(st.nextToken());
                graph[i][j] = weight;
            }
        }
        for(int i = 0; i < n; i++) {
            Arrays.fill(dp[i], INF);
        }

        System.out.println(dfs(0, 1));
    }
}


// 참고 : https://hongcoding.tistory.com/83
// 파이썬 시간초과 -> 자바로 제출
// 파이썬과 똑같이 58% 시간초과.