#!/usr/bin/env python

class Solution:
    def longestPalindrome(self, s):
        def palindromeAt(i, j=None):
            if j is None:
                # palindrome with one center letter
                length = 1
                L = i - 1
                R = i + 1
            else:
                # palindrome with two center letters
                if s[i] != s[j]:
                    return ''
                length = 0
                L = i
                R = j

            while L >= 0 and R < len(s) and s[L] == s[R]:
                length += 2
                L -= 1
                R += 1
            return s[L+1:R]

        longest = ''
        for center in range(len(s)):
            if (center + len(longest) // 2) >= len(s):
                break
            found = palindromeAt(center)
            if len(found) > len(longest):
                longest = found
            if center + 1 < len(s):
                found = palindromeAt(center, center + 1)
                if len(found) > len(longest):
                    longest = found
        return longest

        
def test(algorithm, test_cases):
    for test in test_cases:
        attempt = algorithm(test[0])
        if attempt not in test[1]:
            print(f'Test failed\ninput: {test[0]}\nexpected: {test[1]}\ngot: {attempt}')
        else:
            print(f'Test passed ({test[0]}->{attempt})')

if __name__ == '__main__':
    test_cases = [
            ('babad', {'bab', 'aba'}),
            ('cbbd', {'bb'}),
            ('', {''}),
            ('a', {'a'}),
            ('aaaaab', {'aaaaa'}),
            ('aaaab', {'aaaa'}),
            ('abcabc', {'a', 'b', 'c'}),
            ('ababba', {'abba'}),
            ('', {''}),
    ]
    test(Solution().longestPalindrome, test_cases)
