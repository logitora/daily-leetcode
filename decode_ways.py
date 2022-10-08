"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:
"A" -> 1 ; "B" -> 2 ; ... "Z" -> 26
To decode an encoded message, all the digits must be grouped then mapped back into letters using 
the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
    "AAJF" with the grouping (1 1 10 6)
    "KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
Given a string s containing only digits, return the number of ways to decode it.
The test cases are generated so that the answer fits in a 32-bit integer.
"""
class Solution:
    def numDecodings(self, s:str) -> int:
        if not s or s[0] == "0":
            return 0
        
        dp = [0 for i in range(len(s) + 1)]

        dp[0:2] = [1,1]

        for i in range(2, len(s)+1):
            if 0 < int(s[i-1:i]):
                dp[i] = dp[i - 1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]

"""
0 cannot stand alone
Numbers can only be joined and counted towards the count if they are a valid number
when joined. i.e. 10 <= number <= 26

If the number string starts with 0, the whole string is automatically
invalid, as there is no way to incorporate the 0 in a way that would be accepted.

This method uses bottom up dp. To do this, we have to establish a base case. More on this in a bit.
We will be using slice indexing to compare the numbers to our criteria. Can probably do this with pointers
pointing to the numbers we are looking at.
Starting at i = 2, we will go through the entire string looking at the immediate previous number and the number previous to that one.
In other words, numbers at i-1 and i-2. 
Our for loop range should account for this by stopping at len(s)+1. That way, i will be at len(s) and our slice indexing will compare the very last 2 numbers

But what about the situation where the second number is 0? For example, the given string is "30"
The second number in our dp array is not guaranteed. In the case of "30", there is no valid combination, as 30 is out of the alphabet range and 0 cannot stand alone.
Because of this, we cannot confidently create a base case of size 2.
This is where the base case mentioned earlier comes in. We basically want to have an extra element to account for this edge case, that's why we start the dp array with [1,1]
instead of [1,2] or [0,1].
    Using our [1,1] base case:
    Given string is 30
    i=2: s[i-1:i] is 0. 0 is not < 0, so this step is skipped
    s[i-2:i] is 30. 30 is not in between 10 and 26, so this step is also skipped
    Now we return the last dp element, but right now it is 1. How to fix this problem?
    When making the dp array, just make everything 0 (except for the very first two elements) and replace the values as needed

    If the initial given string is valid like 22
    i=2: s[i-1:i] is 2. 0 < 2, so dp[2] = dp[1] = 1
    s[i-2:i] is 22. 22 is between 10 and 26. dp[2] = dp[2] + dp[i-2] = 2
    In this case, if we were to start our dp as [0,1] or even just not inserted extra space, we would get the wrong answer.

The rest is pretty straight forward dp. If a 0 is encountered, it MUST be immediately after either a 1 or 2, or else the string is invalid and the dp for that index stays 0

Time complexity = O(n) linear because of dp. Only have to go through s[] once
Space complexity = O(n) because of the additional array
"""