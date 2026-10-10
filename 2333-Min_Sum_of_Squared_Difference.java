class Solution {
    public long minSumSquareDiff(int[] nums1, int[] nums2, int k1, int k2) {
        long k = (long) k1 + k2;
        int n = nums1.length;
        int max = 0;
        long total = 0;
        for (int i = 0; i < n; i++) {
            int diff = Math.abs(nums1[i] - nums2[i]);
            max = Math.max(max, diff);
            total += diff;
        }
        if (total <= k) return 0;
        long[] c = new long[max + 1];
        for (int i = 0; i < n; i++) {
            c[Math.abs(nums1[i] - nums2[i])]++;
        }
        long num = 0;
        for (int curr = max; curr >= 1; curr--) {
            num += c[curr];
            if (num == 0) continue;
            if (k >= num) {
                k -= num;
            } else {
                long ans = k * (long) (curr - 1) * (curr - 1)
                         + (num - k) * (long) curr * curr;
                for (int diff = 1; diff < curr; diff++) {
                    ans += c[diff] * (long) diff * diff;
                }
                return ans;
            }
        }
        return 0;
    }
}