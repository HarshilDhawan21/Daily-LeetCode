class Solution {
    public long countCommas(long n) {
        long ans = 0;
        if (n >= 1_000L)                 ans += n - 999L;
        if (n >= 1_000_000L)              ans += n - 999_999L;
        if (n >= 1_000_000_000L)          ans += n - 999_999_999L;
        if (n >= 1_000_000_000_000L)      ans += n - 999_999_999_999L;
        if (n >= 1_000_000_000_000_000L)  ans += n - 999_999_999_999_999L;
        return ans;
    }
}