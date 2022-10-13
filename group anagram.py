"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hsh = {}
        for word in strs:
            combo = "".join(sorted(word))
            if combo not in hsh:
                hsh[combo] = [word]
            else:
                hsh[combo].append(word)
                
        ans = []
        for values in hsh.values():
            ans.append(values)
        return ans
"""
The goal is to group each word into their respective anagram groups. For example, bat and tab would be in a separate group from cat and act.
We can do this with a hashmap. Remember that strings are really just an array of characters, so in order for our answer to be in the correct format,
we have to append the string as a joined object rather than the individual character elements. 
To do this, we assign a variable -- in this case called combo -- to each word/array of characters in strs. This word is sorted and then joined together, assigned
to the variable, and then put into the hashmap. Each different word in the same anagram group will have the same sorted combo, so we can just
append the word into the hashmap value. So the hashmap will be made up of combo keyvalues : list/array of words
Then we make a separate ans array and append all hsh values into the answers array.
Time = O(mn) since the sort function is linear time, but it is not necessarily the same length as the strs array.
Space = O(2n) for the hashmap and answers array
"""