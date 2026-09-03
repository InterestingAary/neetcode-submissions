class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        count = 0
        current = head
        while current:
            count += 1
            current = current.next

        mid = count // 2

        current = head
        for _ in range(mid):
            current = current.next

        return current
