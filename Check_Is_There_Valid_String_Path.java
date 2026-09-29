class Solution {
    private Boolean[][][] list;
    private int row, col;
    private char[][] grid;
    public boolean hasValidPath(char[][] grid) {
        this.grid = grid;
        this.row = grid.length;
        this.col = grid[0].length;
        int tlen = row + col - 1;
        if (tlen % 2 != 0) return false;
        if (grid[0][0] == ')' || grid[row - 1][col - 1] == '(') return false;
        int maxOpen = tlen / 2;
        this.list = new Boolean[row][col][maxOpen + 1];
        return dfs(0, 0, 0, maxOpen);
    }
    private boolean dfs(int r, int c, int openc, int maxOpen) {
        if (grid[r][c] == '(') {
            openc++;
        } else {
            openc--;
        }
        if (openc < 0 || openc > maxOpen) return false;
        if (r == row - 1 && c == col - 1) return openc == 0;
        if (list[r][c][openc] != null) return list[r][c][openc];
        boolean ans = false;
        if (c + 1 < col && dfs(r, c + 1, openc, maxOpen)) ans = true;
        if (!ans && r + 1 < row && dfs(r + 1, c, openc, maxOpen)) ans = true;
        return list[r][c][openc] = ans;
    }
}