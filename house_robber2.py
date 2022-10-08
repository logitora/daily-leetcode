"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, 
adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        
        dp0 = [nums[0], nums[1]] # starts at 0 and will not include the very last nums element (n-1)
        for i in range(2, len(nums)-1):
            temp0 = dp0[:-1]
            dp0.append(nums[i] + max(temp0))
            
        dp1 = [nums[1], nums[2]] # starts at 1 and will include the very last nums element (n-1)
        for i in range(3, len(nums)):
            temp1 = dp1[:-1]
            dp1.append(nums[i] + max(temp1))
        
        max0 = max(dp0[-1], dp0[-2])
        max1 = max(dp1[-1], dp1[-2])
        return max(max0, max1)
"""
Basically the same as House Robber 1 but done twice to account for different starting points.
Since the last house is the neighbor of the first house, we go through the array twice, one which hits the 
very first house but excludes the last house. The other which starts on the second house but hits the very last house.
After setting up those parameters, proceeds as normal like in House Robber 1. This might have some unneccessary variable assignment with max0 and max1, 
but I just did that to be safe. It's probably a negligible optimization. A more significant optimization would be to find a way 
to do this without 2 loops and with only 1 additional array.

Time = O(n) linear dp. Iterate through the array once. Technically O(2n)
Space = O(n) for the two extra arrays. Technically O(2n)
"""