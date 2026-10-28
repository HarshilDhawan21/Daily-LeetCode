class Solution {
    public int minCost(int[][] grid){
        int m = grid.length, n = grid[0].length;
        boolean[][][] dp = new boolean[m][n][1024];
        dp[0][0][grid[0][0]] = true;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) continue;
                int curr = grid[i][j];
                for (int k = 0; k < 1024; k++) {
                    if ((i > 0 && dp[i-1][j][k]) || (j > 0 && dp[i][j-1][k])) {
                        dp[i][j][k ^ curr] = true;
                    }
                }
            }
        }
        for (int k = 0; k < 1024; k++) {
            if (dp[m-1][n-1][k]) return k;
        }
        return -1;
    }
}