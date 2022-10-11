"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
A subarray is a contiguous subsequence of the array.
    1 <= nums.length <= 2 * 104
    -10 <= nums[i] <= 10
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pref,suff = [*nums],[*(reversed(nums))]

        for i in range(1, len(nums)):
            if pref[i-1] != 0:
                pref[i] = pref[i-1] * nums[i]
            else:
                continue

        for j in range(1, len(nums)):
            if suff[j-1] != 0:
                suff[j] = suff[j-1] * nums[-1-j]
            else:
                continue

        return max(max(pref), max(suff))
"""
Prefix and suffix product again, but this time we need more conditions to add. 
The main obstacle that this problem gives us is finding a solution for what will be done when a 0 is encountered while going through the array. 
Another big obstacle is what will we do if negative numbers are encountered. Unlike 0, we can't just discard the subarray when a negative is met, since there's a
chance to encounter another negative number and end up with an even bigger product. 
If a 0 is encountered, we skip it and essentially start building our product result again, using 0 as the end of the subarray. 
We want to use prefix and suffix products to account for differing amounts of negative numbers that would influence the product. The goal is 
to have an even amount of negative numbers as part of the numbers contributing towards the product, since that would result in a positive number.
By starting from opposite ends of the array, we cover our bases for different combinations of even amounts of negative numbers.
To end, we return the max of pref and suff arrays.

Time = O(2n) linear, but we have to iterate through n terms twice, essentially, to get the prefix and suffix products.
Space = O(2n) 2 separate arrays that are basically duplicates of the original array.
"""

"""
There's another DP solution to this too but I'll figure it out when I revisit the problem. DP is probably a little more intuitive and easer to explain.
We can also optimize space since we are only looking at the results of the previous subproblem. Knowing this, there's no need to allocate a whole separate array.
"""