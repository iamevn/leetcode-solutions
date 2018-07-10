#!/usr/bin/env python

"""Given an unsorted integer array, find the smallest missing positive integer.
Your algorithm should run in O(n) time and use constant extra space.
"""

from typing import Callable, Sequence, Tuple, List

# Types
""" TestCase:
(nums, sol)
nums is a sequence of numbers
sol is the expected result
"""
TestCase = Tuple[Sequence[int], int]


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """returns first missing positive integer in nums
        (modifies nums in the process)

        algorithm:
            for each n in nums, swap n to its home
            home is:
                for n < 1, n > len(nums), or duplicates:
                    end of the list (shifting end to the left)
                otherwise:
                    nums[n - 1]

        getting length of nums is constant,
        the inner while loop runs once for each number,
        each number in nums will be swapped up to twice to get home
        need a final walkthrough of nums to find the hole

        reuses nums as storage
        all local variables are constant size

        takes O(n) time
        uses O(1) additional space
        """
        if not nums:
            return 1

        end: int = len(nums) - 1
        for i, n in enumerate(nums):  # for each index in nums
            if i >= end:  # don't reprocess numbers already home
                break
            while n != i + 1 and i < end:  # until nums[i] is home
                if n > len(nums) or n < 1 or n == nums[n - 1]:
                    nums[i], nums[end] = nums[end], nums[i]
                    end -= 1
                else:
                    nums[i], nums[n - 1] = nums[n - 1], nums[i]
                n = nums[i]

        expect: int = 1
        for n in nums:
            if n != expect:
                return expect
            else:
                expect += 1
        return len(nums) + 1


def test(algorithm: Callable, test_cases: Sequence[TestCase]) -> None:
    for test_case in test_cases:
        attempt = algorithm(test_case[0])
        if attempt != test_case[1]:
            print(f'Fail: {test_case[0]} -> {attempt} (expect:{test_case[1]})')
            print(f'got: {attempt}')
        else:
            print(f'Pass {test_case[0]} -> {attempt}')


if __name__ == '__main__':
    test_cases: List[TestCase] = [
            ([1, 2, 0], 3),
            ([3, 4, -1, 1], 2),
            ([7, 8, 9, 11, 12], 1),
            ([], 1),
            ([-1], 1),
            ([0], 1),
            ([1], 2),
            ([3, 2, 1], 4),
    ]
    test(Solution().firstMissingPositive, test_cases)
