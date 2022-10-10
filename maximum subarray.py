"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.
    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max, true_max = 0, (-inf)
        for i in range(len(nums)):
            curr_max += nums[i]
            if curr_max > true_max:
                true_max = curr_max
            if curr_max < 0:
                curr_max = 0
        return true_max
"""
Kadane's algorithm. If local max ever falls below 0, reset it to 0.
Pretty straightforward.
Time = O(n) linear. Goes through the array only once
Space = O(1)
"""