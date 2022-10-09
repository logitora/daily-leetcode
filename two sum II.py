"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. Let these two numbers be 
numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array 
[index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return [i+1, j+1]

"""
Two pointers method. Both pointers start on opposite ends and are moved in. Depending on the conditions, either the left or right pointer moves in.
i = left. j = right. I don't know why I did i and j for my first solution lol.

This method takes advantage of the fact that the array is already sorted in ascending order. If the sum of the two numbers is less than the target, then we want to increment 
the pointer on the smaller side of the array in order to get closer to the target.
Likewise, if the sum overshoots the target, we want to decrement the right pointer to bring it down closer.
The array is 1 indexed so we just return the i and j with 1 added

Time = O(n) linear. Goes through the array once
Space = O(1)
"""