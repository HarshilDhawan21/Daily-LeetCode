class Solution:
    def nodesBetweenCriticalPoints(self, head):
        First = last = prev_pos = -1
        Leastgap = float('inf')
        prev, curr, pos = head, head.next, 1
        while curr and curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val):
                if First == -1:
                    First = pos
                else:
                    Leastgap = min(Leastgap, pos - last)
                last = pos
            prev, curr, pos = curr, curr.next, pos + 1
        return [-1, -1] if First == last else [Leastgap, last - First]