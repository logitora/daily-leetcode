"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr1, ptr2 = head, head
        for i in range(n):
            ptr2 = ptr2.next
        if not ptr2:
            return ptr1.next
        while ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        ptr1.next = ptr1.next.next
        return head
"""
Two pointers. Pointer 2 will be offset by n. Once pointer2 has gone through the linked list n times, we iterate
pointer1 and pointer2 in sync until pointer 2 reaches the end. At this point, pointer 1 will be before the node we want to remove. Just set
ptr1.next to ptr1.next.next to skip over the nth node. If ptr2 ever goes off the list during the offsetting step, like n=len(linkedlist), 
then we return ptr1.next, which would remove the first node. 
Time = O(n)
Space = O(1)
"""