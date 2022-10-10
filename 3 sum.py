"""
Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
    3 <= nums.length <= 3000
    -105 <= nums[i] <= 105
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for left in range(len(nums)-2):
            if left > 0 and nums[left] == nums[left-1]:
                continue
            mid = left + 1
            right = len(nums) - 1
            while mid < right:
                current = nums[left] + nums[mid] + nums[right]
                if current < 0:
                    mid += 1
                elif current > 0:
                    right -= 1
                else: # current = 0
                    ans.append([nums[left], nums[mid], nums[right]])
                    while mid < right and nums[mid] == nums[mid+1]:
                        mid += 1
                    while mid < right and nums[right] == nums[right-1]:
                        right -= 1
                    mid += 1
                    right -= 1
        return ans
"""
The goal is to find 3 numbers that sum up to 0 by using a modified two-pointer method.
First, the array must be sorted, which is an O(n) process right off the bat.
ans is a separate array to keep track of our number combos
We do the same two pointer method except now we have an anchor point set as the left pointer. Mid and right pointers
are what moves in to check the sum of the three numbers.
If left ever iterates to a number that it already has, then the loop continues until another unique number is the anchor point
Depending on the sum, either mid or right pointers will move in. If the sum is < 0, mid comes in closer to bring the sum closer to 0 and vice versa.
Once a valid combination has been found, nums[left], nums[mid], and nums[right] are appended as an array to the ans array. 
Mid and right are moved in to find unique numbers.

Time = O(n^2) left pointer must iterate through the whole loop while mid and right are also iterating through the entire array at the same time
Space = O(n) a separate answers array must be made
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set() # prevents duplicates. answers will be sorted and added
        n,p,z = [], [], [] # divide nums into negative, positive, zeroes
        for num in nums:
            if num == 0:
                z.append(num)
            elif num < 0:
                n.append(num)
            else:
                p.append(num)
        
        neg, pos = set(n), set(p) # look up targets in set O(1)
        
        if z: # adds any answers using one 0
            for num in pos:
                if -1*num in neg:
                    ans.add((-1*num, 0, num))
                    
        if len(z) >= 3: # takes care of the 0,0,0 answer
            ans.add((0,0,0))
            
        for i in range(len(n)): # takes the sum of two negative numbers and finds the complement to the sum in pos
            for j in range(i+1, len(n)):
                target = -1* (n[i] + n[j])
                if target in pos:
                    ans.add(tuple(sorted([n[i], n[j], target])))
                    
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                target = -1* (p[i] + p[j])
                if target in neg:
                    ans.add(tuple(sorted([p[i], p[j], target])))                   
        return ans
"""
A faster runtime method that uses a little more memory. The extra memory includes 3 sets and 3 separate arrays.
The goal of this method is to divide and conquer by splitting the array into negatives, zeroes, and positive numbers. The negatives
and positives are put into sets for O(1) lookup times. 

The first code block @ line 60 is appending any answers that will use 0. If the answer includes 0, then the only way for the other two numbers
to sum up to 0 is if they are complements of each other, in other words, they are the same number of opposite signs.
This is where the constant lookup time of sets/dicts comes in handy to optimize the runtimes. 

Second code block @ line 65 will check and add the 0,0,0 combo to our answers. This is only necessary once

Third code block @ line 68 will loop through the negative numbers array with two pointers and find any numbers in the positive numbers set that will
balance them out to 0. Any valid combos are added to the list.

Fourth code block @ line 74 is the same but for positive numbers.

Notice how answers are added to the set. Since ans is a set, we have to sort the array of answers that we retrieve to be certain that we are not adding duplicate combinations. 
However, in order to add to a set, the object that we are adding must be immutable. So after sorting our answer, we must convert it to a tuple before finally adding to the set,
since tuples are immutable.

Time = O(n^2) sorting is O(n). Iterating through the negative and positive arrays is O(n^2), however the optimization comes from the constant lookup time in our sets
Space = O(n^2) separate arrays for negative, 0, and positives, along with sets for negatives, positives, and triplet answers.
"""