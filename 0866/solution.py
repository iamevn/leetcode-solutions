#!/usr/bin/env python

from math import ceil, floor, sqrt

def palindromes(n: int) -> int:
    """yield successive palindromes starting at n"""
    # 1 -> 2 -> 3 ... 9 -> 11 -> 22 -> 33 -> 44 .. 99 -> 101
    # 101 -> 111 -> 121 -> 131 -> ... -> 191 -> 202 -> 212
    # 989 -> 999 -> 1001 -> 1111 -> 1221
    # 9889 -> 9999 -> 10001 -> 10101 -> 10201
    prev = n
    s = str(n)
    even = len(s) % 2 == 0
    s = s[:ceil(len(s) / 2)]
    n = int(s)
    while True:
        if even:
            pal = int(''.join([s, s[-1::-1]]))  # join '12' with '21'
        else:
            pal = int(''.join([s, s[-2::-1]]))  # join '12' with '1'
        if prev <= pal:
            yield pal
 
        n += 1
        if all(digit == '9' for digit in s):
            even = not even
            if even: n //= 10
        s = str(n)

def isPrime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
        

class Solution:
    def primePalindrome(self, N: int) -> int:
        """return lowest prime palindrome >= N"""
        for p in palindromes(N):
            if isPrime(p):
                return p
