"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing 
together the nodes of the first two lists.
Return the head of the merged linked list.
    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                tail = list1
                list1 = list1.next
            else:
                tail.next = list2
                tail = list2
                list2 = list2.next
        tail.next = list1 or list2
        return dummy.next
"""
Uses the two list pointers, tail and a dummy node to merge the two lists. The purpose of the dummy node is to create a new starting point for the merged list.
We compare the values at list1 and list2 and move tail to the lesser value, where we will stitch it together with dummy as the start. Once list1 or list2
exhausts all options in their respective linked lists, tail will stitch together the rest of the other list.
Time = O(mn)
Space = O(1)
"""