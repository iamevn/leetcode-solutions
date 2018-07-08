#!/usr/bin/env python

class Solution:
     def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str

        the conversion goes as so:
        first numRows letters straight down,
        then numRows - 2 letters diagonally back up to top row,
        then numRows letters straight down,
        etc

        numRows = 3:
        0   4   8
        1 3 5 7 9
        2   6  10

        numRows = 4:
        0     6    12
        1   5 7  11 3
        2 4   8 0  14
        3     9    15
        """
        # edge case
        if numRows == 1:
            return s

        res = ''
        for n in range(numRows):
            x = 0
            while(len(res) < len(s)):
                # vertical numbers
                idx = n + x * ((numRows - 1) * 2)
                if idx >= len(s):
                    break
                res += s[idx]
                # diagonal numbers on all but first and last rows
                if n != 0 and n != (numRows - 1):
                    idx += 2 * (numRows - 1 - n)
                    if idx >= len(s):
                        break
                    res += s[idx]
                x += 1
        return res

               
def test(algorithm, test_cases):
    for test in test_cases:
        attempt = algorithm(*test[0])
        if attempt not in test[1]:
            print(f'Test failed\ninput: {test[0]}\nexpected: {test[1]}\ngot: {attempt}')
        else:
            print(f'Test passed ({test[0]}->{attempt})')

if __name__ == '__main__':
    test_cases = [
            (("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR"),
            (("PAYPALISHIRING", 4), "PINALSIGYAHRPI"),
            (("A", 1), "A"),
            (("A", 5), "A"),
            (("", 3), ""),
            (("AB", 1), "AB"),
            (("AB", 3), "AB"),
            (("ABCD", 2), "ACBD"),
    ]
    test(Solution().convert, test_cases)
