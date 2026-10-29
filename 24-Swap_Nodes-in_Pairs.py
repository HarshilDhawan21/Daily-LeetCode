class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        _ = ListNode(0, head)
        prev = _
        while prev.next and prev.next.next:
            a = prev.next
            b = a.next
            a.next = b.next
            b.next = a
            prev.next = b
            prev = a
        return _.next