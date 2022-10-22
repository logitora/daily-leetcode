"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
    The number of nodes in the list is in the range [1, 105].
    0 <= Node.val <= 9
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast, curr = head, head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        stack = [slow.val]
        while slow.next:
            slow = slow.next
            stack.append(slow.val)
        while stack:
            if stack.pop() != curr.val:
                return False
            curr = curr.next
        return True
"""
First we must find the middle of the linked list. We do this by using a fast and slow pointer, with the fast pointer moving two nodes for the slow's one. This will be the only
purpose of the fast pointer. Once the center is found, we make a stack/array starting with the center value and start appending as we iterate the slow pointer. This stack will serve
as a last in, first out method, since we will be iterating through the first half again and popping the most recent value. This is effectively comparing the first half 
of the linked list to the reverse of the second half. Another way to think about it is bringing two pointers from either end together and comparing the values.
Time = O(n)
Space = O(1)
"""