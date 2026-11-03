class Solution {
    public int minMoves(int[] nums) {
        int max = 0, s = 0;
        for (int x : nums) {
            max = Math.max(max, x);
            s += x;
        }
        return max * nums.length - s;
    }
}