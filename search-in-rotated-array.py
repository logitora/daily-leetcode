"""
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target:
            return 0

        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        piv = left
        left, right = 0, len(nums)-1
        if target >= nums[piv] and target <= nums[right]:
            left = piv
        else:
            right = piv
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
"""
First block of code is some pre processing.
Second block is a binary search to find the pivot point like in "Finding the min in a rotated array"
We find the pivot point in order to split the array into 2 subarrays
Keep track of the pivot point's index with piv
Set up another binary search, we will decide which subarray to search based on its value
    if target >= nums[piv] and target <= nums[right]
    i.e. if the target is on the right subarray
    if target is >= nums[piv] but > nums[right], then it is in the left subarray, since those are made up of greater valued numbers that got wrapped around
    If target is in the array, it should always be greater or equal to the pivot point, since the pivot point is the lowest value
Depending on which, set piv to left or right and proceed with binary search as usual.
Time = O(n)
Space = O(1)
"""
class Solution:
    def search_using_inf(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target:
            return 0

        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right - left) // 2
            comp = nums[mid]
            if (nums[mid] >= nums[0] and target >= nums[0]) or (nums[mid] < nums[0] and target < nums[0]):
                comp = nums[mid]
            else:
                if target < nums[0]: 
                    comp = -inf
                else:
                    comp = inf
            
            if target == comp:
                return mid
            if target > comp:
                left = mid + 1
            else:
                right = mid - 1
        return -1
"""
A clever method found that basically takes out the binary search for finding the pivot point.
In this method, we use a separate variable, comp, to keep track of the number value at mid and compare to target
We also take advantage of the fact that if the array is rotated, nums[0] ends up being higher than nums[n]
    if (nums[mid] >= nums[0] and target >= nums[0]) or (nums[mid] < nums[0] and target < nums[0]):
    This is basically asking "is mid and target on the same side of the pivot point?" without explicitly finding the pivot point
    nums[mid] >= nums[0] and target >= nums[0] means they are both on the left side of the pivot point, since every number after the pivot point will be less than nums[0]
    nums[mid] < nums[0] and target < nums[0] means they are both on the right side of the pivot point, since all of those numbers will be smaller than nums[0]
Pay attention to the inequality operators! We want to make sure to search the left side if nums[mid] is greater than OR EQUAL TO nums[0]
If we used <= and target is the same value as nums[0], then we would search the wrong side
Anyway, here's the actual clever part. It's basically what we do if target and mid are on different sides of the array
    if target < nums[0]
    i.e. if target is on the right side and mid is on the left
If this is the case, we just set our comp variable to -inf, since everything to the left of mid is automatically eliminated from consideration
The same applies to if target is on the left side, except comp is set to inf
The rest is just regular binary search except target is being compared to comp now instead of explicitly nums[mid]
We could take this a step further and just change the values in the original nums array, since depending on the conditions
everything to the left or right of mid is ignored. Doing it this way would get rid of the use of comp and let us go back to 
comparing to nums[mid].
This method ended up being the same runtime as the one above, but I just thought it was a cool and clever method that was worth keeping track of
Time = O(n)
Space = O(1)
"""