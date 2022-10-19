"""
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
    The number of nodes in the list is in the range [1, 100].
    1 <= Node.val <= 100
"""
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = fast
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
"""
Since fast will move at twice the rate of slow, once fast reaches the end, slow will be in the middle of the list.
Time = O(n)
Space = O(1)
"""