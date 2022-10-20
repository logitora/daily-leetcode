"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        p1 = dummy
        carry = False
        while l1 or l2:
            add = (l1.val if l1 else 0) + (l2.val if l2 else 0)
            if carry:
                add += 1
            if add >= 10:
                carry = True
            else:
                carry = False
            p1.next = ListNode(add%10, None)
            p1 = p1.next
            l1, l2 = (l1.next if l1 else None), (l2.next if l2 else None)
        if carry:
            p1.next = ListNode(1, None)
        return dummy.next
"""
Dummy node is needed as a start for our new linked list, which will represent the sum of the two linked lists. Since l1 and l2 are arranged in reverse order, 
it will make "carrying the 1" a little easier in our operations.
In order to keep track of if we need to carry the 1, I set up a bool variable to denote if a sum went over 10. If it is true, then 1 will be added to the sum 
in the next loop. Then, if the sum is below 10, it will be set to false. 
The while loop goes until l1 and l2 are both invalid. To prevent a NoneType error, I did a pythonic function for getting our add sum variable.
    l1.val if l1 else 0
The syntax is pretty straightforward. Then if carry is true, 1 is added. We want to make sure to put this before checking if add goes over 10 or not, since the 1 
is carried over to the next number. If we had put this after the check, then 1 would be added to our current sum, which would be incorrect. 
After the checks are done, we make a new node and set it as p1.next. The val of the new node will be our add variable % 10, since this will take the right most digit
in the case of the answer being 2 digits. If it is 1 digit then it will just return the answer anyway.
Then, we move p1 up as well as l1 and l2. Again, I used pythonic syntax for this, but its pretty straightforward. In the cse that l1 or l2 is invalid or points to None,
then we just set them to None. This, again, avoids a NoneType error when trying to access .next on None.
Once l1 and l2 are exhausted, if carry is still true, then we have to make a final new node with just the value 1.
The main things to note is how the handle when one linked list ends early. In this case, we use the inline if-else statements for grabbing the list values and also 
did something similar for iterating the list pointers to the next node. 
Time = O(mn)
Space = O(1) since the additional linked list that we return does not count. If it does count then this would be O(n)
"""