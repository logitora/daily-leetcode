"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, 
and return the reversed list.
    The number of nodes in the list is n.
    1 <= n <= 500
    -500 <= Node.val <= 500
    1 <= left <= right <= n
"""
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        p1 = dummy
        for i in range(left-1):
            p1 = p1.next
        p2 = p1.next
        for i in range(right-left):
            temp = p1.next
            p1.next = p2.next
            p2.next = p2.next.next
            p1.next.next = temp
        return dummy.next
"""
First, traverse p1 {left-1} times to get to the node right before left. Left is the first node in the subarray that will eventually be moved to before {right}.
p2 is after p1, which is also left.
Perform a for loop that will iterate as many times needed to get through the subarray between right and left inclusive. This part is a little difficult to grasp (at least for me) so 
I will try to extensively write out what happens.
FIRST we must make a temp variable that will keep track of our first node after p1. This is because eventually it will momentarily be the head of the sub linked list with no way to 
access it. 
SECOND we set p1.next to the node after p2. Remember, p2 will be moving along the list since it is stuck to our node denoted by {left}. At this point, the node after p1
will have no link leading to it. In the first iteration, p2 will still denote the node after p1, but after this loop, there will be no variable "stuck" onto the node after p1
if we didn't make copy it into a temp variable. This is why the temp variable is needed. 
THIRD we skip p2.next and link p2 to the node after p2.next.
FOURTH we connect our temp variable/node. At this point, the whole list is connected again. 
This loop continues until right is reached
ex after the first for loop:
    D => 1 => 2 => 3 => 4 => 5      left=2, right=4, temp = 2 In the first loop this happens to be p2, but later on it won't be!
         p1  p2                     temp = p1.next
    D => 1    2 => 3 => 4 => 5      
         p1---p2---^                p1.next = p2.next Notice how node 2 has no connection towards it. Later on, when the disconnected node is not p2, it will be easier to see why temp is needed

              |---------v
    D => 1    2    3 => 4 => 5      p2.next = p2.next.next
         p1---p2---^
    
              |---------v
    D => 1    2 <= 3 => 4 => 5      p1.next.next = temp
         p1---p2---^
    reorderd after first loop:
    D => 1 => 3 => 2 => 4 => 5      Notice how p2 stuck with node 2/left after the reordering. Now it is easier to see why we need a temp variable!
         p1       p2      
Time = O(n)
Space = O(1)
"""