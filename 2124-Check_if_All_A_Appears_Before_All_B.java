class Solution {
    public boolean checkString(String s) {
        boolean done = false;
        for (char i : s.toCharArray()) {
            if (i == 'b') {
                done = true;
            } else if (done) {
                return false;
            }
        }
        return true;
    }
}