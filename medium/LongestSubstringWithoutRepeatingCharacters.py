'''
https://leetcode.com/problems/longest-substring-without-repeating-characters

Problem:
    Given a string s, find the length of the longest substring without repeating characters.

Complexity:
    Time Complexity: O(n) – We iterate through the string exactly once using the sliding window technique, where n is the length of the string. 
    Space Complexity: O(min(m, n)) – We use a hash map to store the last seen indices of characters, where m is the size of the character set and n is the length of the string.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = {}  # stores most recent index of each character
        max_length = 0
        start = 0  # left pointer 
        
        for end, char in enumerate(s): # right pointer & curr char
            # if character is in window, move the left pointer
            if char in char_dict and char_dict[char] >= start:
                start = char_dict[char] + 1
            
            # update latest position of char
            char_dict[char] = end
            
            # update max_length with window size if larger
            max_length = max(max_length, end - start + 1)
            
        return max_length
