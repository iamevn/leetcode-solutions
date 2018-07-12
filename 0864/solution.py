#!/usr/bin/env python

"""Given a blacklist `B` containing unique integers from `[0, N)`,
write a function to return a uniform random integer from `[0, N)`
which is **NOT** in `B`.

Optimize it such that it minimizes the call to system's `Math.random()`.
"""

from typing import List
from random import randint


class Solution:
    """generate random integers not in a blacklist

    accomplishes this by building a map of blacklisted numbers to safe numbers
    generates a random number in range [0, N - len(blacklist))
    if this number is blacklisted, check mapping for safe number to use
    all numbers in mapping below that cap map to a safe number above the cap
    all numbers in mapping above that cap map to themselves

    no two blacklisted numbers map to the same number
    no blacklisted number maps to something in the range of the randint call
    because blacklist must contain unique numbers below N, the mapping from
      blacklisted numbers to safe numbers along with safe numbers below the cap
      covers the full range from [0, N)

    B = len(blacklist)

    __init__ spends most of its time building the mapping
    swapping elements in blacklist around to ensure correct mapping
      takes O(1) work up to B times
    checking that there are no repeats in blacklist takes O(B) time

    pick() makes a single call to random.randint and does one dictionary lookup
    is O(1) time

    the set for checking for repeats takes O(B) space,
    the blacklist mapping takes O(B) space,
    all other variables take O(1) space

    building the object takes O(B) time and O(B) space
    calliing pick takes O(1) time and O(1) extra space
    1 call of Math.random for each pick()
    """
    def __init__(self, N: int, blacklist: List[int]) -> None:
        blackset = set(blacklist)
        if len(blackset) != len(blacklist):
            raise ValueError('blacklist must not have repeated values')
        if any(b >= N for b in blacklist):
            raise ValueError('blacklist must only contain values less than N')
        if len(blacklist) >= N:
            raise ValueError('blacklist must not cover entire range [0, N)')

        cap = N - len(blacklist)
        for i, _ in enumerate(blacklist):
            while blacklist[i] >= cap and blacklist[i] != i + cap:
                b = blacklist[i]
                blacklist[b - cap], blacklist[i] = blacklist[i], blacklist[b - cap]
        blackmap = {n: i + cap for i, n in enumerate(blacklist)}

        assert all(blackmap[key] not in blackmap
                   or blackmap[key] == key
                   for key in blackmap)

        self._blackmap = blackmap
        self._rand = lambda: randint(0, cap - 1)

    def pick(self) -> int:
        r = self._rand()
        if r in self._blackmap:
            r = self._blackmap[r]

        assert r not in self._blackmap

        return r
