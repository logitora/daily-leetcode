"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
Do not modify the linked list.
    The number of the nodes in the list is in the range [0, 104].
    -105 <= Node.val <= 105
    pos is -1 or a valid index in the linked-list.
"""
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    fast = fast.next
                    slow = slow.next
                return slow
        return None
"""
This two pointer method depends on knowing some math with the fast and slow pointers. Basically, when the slow and fast pointers meet the first time, they meet halfway through
the cycle. After a cycle is detected, bring slow back to head and increment both one by one. The two pointers will end up meeting at the beginning of the loop/cycle
Time = O(n)
Space = O(1)
"""
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        while head:
            if head in seen:
                return head
            seen.add(head)
            head = head.next
        return None
"""
Pretty straightforward. Once the head pointer loops back, it the node would have already been added to the set. Set lookup is constant time.
Time = O(n)
Space = O(n)
"""