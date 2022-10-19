"""
You are given the head of a singly linked-list. The list can be represented as:
    L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
    The number of nodes in the list is in the range [1, 5 * 104].
    1 <= Node.val <= 1000
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        rev = None # middle of array. reverse the subarray after mid
        while slow:
            x = slow
            slow = slow.next
            x.next = rev
            rev = x
        # rev is the start of our new reversed subarray
        ptr1 = head.next
        ptr2 = rev.next
        while ptr2:
            head.next = rev
            rev.next = ptr1
            head = ptr1
            rev = ptr2
            ptr1 = ptr1.next
            ptr2 = ptr2.next
"""
This problem basically combines everything we used from the other linked list questions (middle, reverse, and merge linked lists).
First, we want to get the middle of the linked list. We do this the same way we did the middle of the linked list problem. Then, we reverse the right side subarray
to make for proper merging. After reversing the subarray, we then start to merge the two lists, alternating between the left subarray and the reversed
right subarray. We make two pointers, ptr1 and ptr2 to point to the beginning of the left and right subarrays respectively. Since we do not have to return
the linked list head, we can use the original head pointer to work with the data. Head will be behind ptr1, and rev will be behind ptr2. Ptr1 and ptr2 basically act to keep our place 
in the respective linked lists.
Time = O(n) Iterate through half of the list to get the middle, go through the right subarray to reverse. Then finally iterate through the entire list to stitch it together properly
Space = O(1)
"""