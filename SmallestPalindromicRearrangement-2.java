class Solution {
    public String smallestPalindrome(String s, int k) {
        int len=s.length();
        int lenHalf=(len>>1);
        char mid = (len % 2 == 1) ? s.charAt(lenHalf) : ' ';
        int count[]=new int[26];
        for(int i=0;i<len;i++){
            if ((len & 1) == 1 && i == lenHalf){
                continue;
            }
            count[s.charAt(i)-'a']++;
        }
        for(int i=0;i<26;i++){
            count[i]=count[i]>>1;
        }
        if (totalWays(count, k) < k) {
            return "";
        }
        StringBuilder halfRes=new StringBuilder();
        int half=lenHalf;
        for(int i=0;i<half;i++){
            for(int j=0;j<26;j++){
                if(count[j]>0){
                    count[j]-=1;
                    long ways=1;
                    int letters=0;
                    for(int c=0;c<26;c++){
                        letters+=count[c];
                    }
                    for(int c=0;c<26;c++){
                        if(count[c]>0){
                            ways*=nCr(letters,count[c],k);
                            letters-=count[c];
                        }
                        if(ways>=k){
                            break;
                        }
                    }
                    if(ways>=k){
                        halfRes.append((char)(j + 'a'));
                        break;
                    }
                    k-=ways;
                    count[j]+=1;
                }
            }
        }
        if(mid!=' '){
            return halfRes.toString()+mid+halfRes.reverse().toString();
        }

        return halfRes.toString()+halfRes.reverse().toString();
    }
    private long nCr(int n,int r,int k){
        r=Math.min(r,(n-r));
        long res=1;
        for(int i=1;i<=r;i++){
            res = res * (n - i + 1) / i;
            if(res>=k){
                return (long)k;
            }
        }
        return res;
    }
    private long totalWays(int[] count, int k) {
    int letters = 0;
    for (int x : count) {
        letters += x;
    }
    long ways = 1;
    for (int c : count) {
        if (c == 0) continue;
        ways *= nCr(letters, c, k);
        if (ways >= k) return k;
        letters -= c;
    }
    return ways;
}
}