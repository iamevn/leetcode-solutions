#!/usr/bin/env python

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        start, end = 0, 0
        seen = set()

        while end < len(s):
            next = s[end]
            if next in seen:
                longest = max(longest, end - start)
                while s[start] != next:
                    seen.remove(s[start])
                    start += 1
                start += 1
            else:
                seen.add(next)
            end += 1

        return max(longest, end - start)

""" notes:
brute force solutions involving iterating through all substrings, checking if they have repeating chars and keeping track of the longest

maybe a better solution where we can walk through the string

two ptrs, start and end, both init to 0 (pointing at first letter)
keep track of seen letters in a hashset
keep track of length of longest non repeating substring (now 1)
advance end ptr, has that letter been seen?
 y: longest = max(longest, end - start)
    advance start ptr past where we last saw that letter removing values start ptr passes from set
 n: add to set
when end ptr advances past end, return max length found
"""
        
def test():
    s = Solution()
    tests = [('abcabcbb', 3),
            ('bbbbb', 1),
            ('pwwkew', 3),
            ('aabcadebefacdd', 6),
            ('f', 1),
            ('', 0),
    ]

    for test in tests:
        attempt = s.lengthOfLongestSubstring(test[0])
        if attempt != test[1]:
            print(f'Test failed\ninput: {test[0]}\nexpected: {test[1]}\ngot: {attempt}')

if __name__ == '__main__':
    test()
