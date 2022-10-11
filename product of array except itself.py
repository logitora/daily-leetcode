"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for n in nums] # set up answers array
        left, right = 1,1
        
        for i in range(len(nums)):
            ans[i] *= left
            left *= nums[i]
        
        for j in range(len(nums)):
            ans[-1-j] *= right
            right *= nums[-1-j]
            
        return ans
"""
This method takes the prefix and suffix products to find the product of a whole array except for the current index.
The answers array will be recording the answers for each corresponding number in the numbers array in the same index.
To sort of visualize, the prefix will cover the product for all numbers except at the current index. Likewise with the suffix product.
When these two "meet," it will have covered the whole array except for the current index.
Time = O(2n) still linear, but we only have to go through the array twice, once for acquiring the prefix and suffix products.
Space = O(1)
"""