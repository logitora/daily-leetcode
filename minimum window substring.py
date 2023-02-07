"""
Given two strings s and t of lengths m and n respectively, return the minimum window
substring
of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Constraints:
    m == s.length
    n == t.length
    1 <= m, n <= 105
    s and t consist of uppercase and lowercase English letters.
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hsh = {}
        for c in t:
            if c not in hsh: hsh[c] = 1
            else: hsh[c] += 1
        left, right, window, track, sub  = 0, 0, len(s)+1, len(t), ""
        while right < len(s):
            if s[right] in hsh:
                if hsh[s[right]] > 0: 
                    track -= 1
                hsh[s[right]] -= 1
            while track == 0:
                if (right-left+1) < window:
                    window = right-left+1
                    sub = s[left:right+1]
                if s[left] in hsh:
                    hsh[s[left]] += 1
                    if hsh[s[left]] > 0: 
                        track += 1
                left += 1
            right += 1
        return sub
"""
We store the frequency of letters in t in hsh. 
We use left and right pointers to indicate the bookends of our window/substring
Window is just used to check conditions
Track is set to the length of t. This will only decrement and increment when a letter that is in t is added or subtracted from hsh, a maximum of times that
it appears in t. In other words:
    t = abcc
    track = 4
    hsh = {a:1, b:1, c:2}
    s = aabbbcc
    The amount of a's in s > a's in t, but track will only decrement when going over one a, since only one a appears in t. That is why we must first check if 
    the count in hsh is greater than 0. If the count is below 0, then the count in s of that letter is considered extra and will not effect track
We only started reducing the window once track == 0, in other words, once all letters in t have been found in s.
Update window size and the substring that makes up that window
Starts reducing the window, only stopping once track is greater than 0, meaning the window is now missing some letter that is in t.
Time = O(m+n)
Space = O(n)
"""