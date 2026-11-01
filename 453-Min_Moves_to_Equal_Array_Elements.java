class Solution {
    public int minMoves(int[] nums) {
        int min = Integer.MAX_VALUE;
        long sum = 0;
        for (int n : nums) {
            sum += n;
            min = Math.min(min, n);
        }
        return (int) (sum - (long) nums.length * min);
    }
}