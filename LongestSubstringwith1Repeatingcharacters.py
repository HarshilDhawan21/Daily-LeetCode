class Solution:
    def _build(self, node: int, l: int, r: int) -> None:
        if l == r:
            self.pre[node] = 1
            self.suf[node] = 1
            self.main[node] = 1
            return
        mid = (l + r) >> 1
        self._build(node << 1, l, mid)
        self._build(node << 1 | 1, mid + 1, r)
        self._push_up(node, l, r)
    def _push_up(self, node: int, l: int, r: int) -> None:
        left = node << 1
        right = node << 1 | 1
        mid = (l + r) >> 1
        len_l = mid - l + 1
        len_r = r - mid
        self.pre[node] = self.pre[left]
        self.suf[node] = self.suf[right]
        self.main[node] = max(self.main[left], self.main[right])
        if self.a[mid] == self.a[mid + 1]:
            if self.pre[left] == len_l:
                self.pre[node] = len_l + self.pre[right]
            if self.suf[right] == len_r:
                self.suf[node] = len_r + self.suf[left]
            self.main[node] = max(self.main[node], self.suf[left] + self.pre[right])
    def _update(self, node: int, l: int, r: int, i: int) -> None:
        if l == r:
            return
        mid = (l + r) >> 1
        if i <= mid:
            self._update(node << 1, l, mid, i)
        else:
            self._update(node << 1 | 1, mid + 1, r, i)
        self._push_up(node, l, r)
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        self.n = n = len(s)
        self.pre = [0] * (n << 2)
        self.suf = [0] * (n << 2)
        self.main = [0] * (n << 2)
        self.a = list(s)
        self._build(1, 0, n - 1)
        k = len(queryIndices)
        ans = [0] * k
        for i in range(k):
            index = queryIndices[i]
            self.a[index] = queryCharacters[i]
            self._update(1, 0, n - 1, index)
            ans[i] = self.main[1]
        return ans