def maximumLengthSubstring(s: str) -> int:
    c={}
    left=0
    length=0
    for right in range(len(s)):
        a=s[right]
        c[a]=c.get(a, 0) + 1
        while c[a] > 2:
            left_a=s[left]
            c[left_a]-=1
            left+= 1
        length=max(length,right-left+1)
    return length