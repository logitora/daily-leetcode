"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicates = set()
        for num in nums:
            if num in duplicates:
                return True
            duplicates.add(num)
        return False
"""
Really straightforward. Initialize a set and then start adding numbers in the array to the set while checking if that number is in the set.
Since set lookup time is constant, this would just be linear runtime. 
A more space efficient way would be to sort the array and run through it while comparing i to i-1 but that would come at a cost of runtime, since we would have to sort then iterate
Time = O(n)
Space = O(n)
"""