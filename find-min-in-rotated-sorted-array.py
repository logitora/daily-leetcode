"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.
Constraints:
    n == nums.length
    1 <= n <= 5000
    -5000 <= nums[i] <= 5000
    All the integers of nums are unique.
    nums is sorted and rotated between 1 and n times.
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            if nums[mid] > nums[left]:
                left = mid + 1
            else:
                right = mid
"""
Binary search
The minimum value is the pivot point of the array.
In a normal, unrotated array, the left most number will ALWAYS be less than the right most number since it is sorted.
We can use this to our advantage when trying to find the pivot point.
In a rotated array, the pivot point would be less than the number before it AND after it
So we have if statements that will eventually trigger when a mid point that satisfies one of the two is found
    if nums[mid] < nums[mid - 1] This triggers if our mid point is the true pivot point
    if nums[mid] > nums[mid + 1] This triggers if our mid point is the greatest value, since numbers SHOULD always be less than the number after it

Time = O(log n) binary search
Space = O(1) 
"""