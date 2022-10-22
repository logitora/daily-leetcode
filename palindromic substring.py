"""
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.
    1 <= s.length <= 1000
    s consists of lowercase English letters.
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
        ans = 0
        for i in range(len(s)):
            ans += expand(i, i)
            ans += expand(i, i+1)
        return ans

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = len(s)
        for i in range(len(s)-1):
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        for j in range(1, len(s)):
            left, right = j-1, j+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count
"""
A recursive and iterative version of the same concept. These two methods both use the center expansion method, and must account for odd and even lengthed substrings.
Odd lengthed substrings will have one center letter, while even length substrings will have 2 center letters. If the middle letter(s) are palindromic, then we use left
and right pointers to expand out from the center letter(s). If they are equal, then that substring is palindromic, and we add to the count. We continue until left and right pointers
are not pointing to the same character. The recursive version ran slower than the iterative version, but is written cleaner than the iterative version.
Time = O(n)
Space = O(1)
"""