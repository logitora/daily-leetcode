"""
Given a string s, return the longest palindromic substring in s.
A string is called a palindrome string if the reverse of that string is the same as the original string.
    1 <= s.length <= 1000
    s consist of only digits and English letters.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        i, j = 0, len(s)-1
        
        if len(s) == 1:
            return s[0]
        longest = s[0]
        while i < len(s):
            while j > i:
                if s[i] == s[j]:
                    compare = s[i:j+1]
                    if compare == compare[::-1] and len(longest) < len(compare):
                        longest = compare
                j -= 1
            i += 1
            j = len(s)-1
        return longest
"""
This one is the slower solution but it doesn't use recursion. This was my first solution.
Use two pointers on either side. If the pointers point to the same character, assign the substring to a variable.
Compare the variable with the reverse version. If it is a valid palindrome, check to see if it is longer than the last longest palindrome substring.
Once j goes through the string, iterate i up. 
Time = O(n^2) we are testing every endpoint combination.
Space = O(1)
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            longest = max(self.recursive(s, i, i), self.recursive(s, i, i+1), longest, key=len)
        return longest
            
    def recursive(self, s, left, right):
        while 0 <= left and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
"""
Faster solution using recursion. Start by establishing a longest variable to keep track of whatever longest palindrome substring we come across.
For loop through the string and returning the longest palindrome substring. 
This method uses the "grow from center" method. I don't know if there's a proper name for it but that's basically what the methodology is. 
To account for palindromes that are odd or evenly lengthed, we pass in i,i and i,i+1. These two combinations represent the mid point for odd lengthed and 
even lengthed palindromes respectively. Call the recursive function with the key to return based on str length. Once left != right, we return the substring that was valid.
Time = O(n^2) worst case. Recursive function is about 0.5n since at worst it will spread from the very center all the way to the end.
Space = O(1)
"""