"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
    The number of the nodes in the list is in the range [0, 104].
    -105 <= Node.val <= 105
    pos is -1 or a valid index in the linked-list.
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        fast, slow = head.next, head
        while fast and fast.next:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False
"""
Use two pointers, one slow, one fast. The slower pointer will iterate once each cycle. The faster pointer will iterate twice
a cycle. If there is a cycle, the two pointers will eventually meet up again as the fast pointer laps the slow pointer. If
there is no cycle, the fast pointer will just reach the end.
Time = O(n)
Space = O(1)
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
"""
A faster solution which uses more space. This just iterates through the entier linked list and puts each node into a set, which doesn't allow for duplicates. 
Sets have constant look up time.
Time = O(n)
Space = O(1)
"""