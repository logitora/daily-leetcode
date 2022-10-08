"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from 
robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken 
into on the same night. Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight 
without alerting the police.
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        dp = [nums[0], nums[1]]
        for i in range(2, len(nums)):
            temp = dp[:-1]
            dp.append(nums[i] + max(temp))
        return max(dp[-1], dp[-2])
"""
Bottom up tabulation dp.

Edge cases were basically what should we do when we encounter a house denoted with 0?
By making temp an identical array excluding the immediate previous house, we can start making a path
that will optimize for the highest amount. This way, any paths that hit the "0 house" will either be ignored
or incorporated if it lead to a greater sum later on down the line.
Since we are excluding the last house, either the last or second to last element will be the greatest sum value. 

Time complexity = O(n) tabulation dp. Only have to iterate through the array once
Space = O(n) We have to make a completely separate dp array. The next solution is an in-place method and will be O(1)
"""
class Solution:
    def rob_add(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        nums = [0,0,0] + nums
        for i in range(3, len(nums)):
            before2 = nums[i] + nums[i-2]
            before3 = nums[i] + nums[i-3]
            nums[i] = max(before2, before3)
        return max(nums[-1], nums[-2])
"""
This solution follows the same line of thinking as the above solution but does it in place of the original nums array.
before2 and before3 are pointers that point to the houses 2 steps before or 3 steps before, since we cannot come from the immediately previous house.
We want to add the additional 3 0's to account for the fact that our pointers are looking back 3 houses.
Starting at i=3 will start us at the first house in the original nums array. Since this is the first house, there is nothing to add to the sum.
Doing it this way guarantees that we are not skipping any houses in the beginning.

Time = O(n) for the same reasons above
Space = O(1) since this replaces the values inside of the original nums value. The additional 3 0 elements are technically added space but...
"""