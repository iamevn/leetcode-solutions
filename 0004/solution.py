#!/usr/bin/env python

from math import floor

def merge(l1, l2):
    """
    :type l1: List[int]
    :type l2: List[int]
    :rtype: List[int]

    merge sorted input into sorted output
    """
    out = []
    while l1 and l2:
        if l1[0] <= l2[0]:
            out.append(l1.pop(0))
        else:
            out.append(l2.pop(0))
    while l1:
        out.append(l1.pop(0))
    while l2:
        out.append(l2.pop(0))
    return out

def get_nth(nums1, nums2, n):
    l1, l2 = 0, 0

    while n > 0 and l1 < len(nums1) and l2 < len(nums2):
        m1 = min(len(nums1) - l1, (n + 1) // 2)
        mid1 = nums1[l1 + m1 - 1]
        m2 = min(len(nums2) - l2, (n + 1) // 2)
        mid2 = nums2[l2 + m2 - 1]

        if mid1 <= mid2:
            n -= m1
            l1 = m1 + l1
        else:
            n -= m2
            l2 = m2 + l2

    if l1 == len(nums1):
        return nums2[l2 + n]
    if l2 == len(nums2):
        return nums1[l1 + n]
    else: # n == 0
        return min(nums1[l1], nums2[l2])

"""
Initial solution does not meet O(log(n+m)) complexity requirement, is O(n+m) 
could get that style of solution down to O((n+m)/2) by just walking that many elements through the lists but still not good enough

in order to reach logarithmic time complexity we need to divide the solution up and only look at the parts we care about

what do we know about median?
- is either one of the elements or is the average of two elements
- splits sequence of numbers into even halfs
- need to pick out nth biggest element from 2 sorted arrays
- divide each array in 2, can eliminate elements too small or too large to be median
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1, len2 = len(nums1), len(nums2)
        total_len = len1 + len2

        return (get_nth(nums1, nums2, total_len // 2) + get_nth(nums1, nums2, (total_len - 1) // 2)) / 2

    def initialSolution(self, nums1, nums2):
        merged = merge(nums1, nums2)
        mid = len(merged) / 2
        if mid % 1 == 0:
            # had even length
            mid = int(mid)
            return (merged[mid] + merged[mid - 1]) / 2
        else:
            # had odd length
            return merged[floor(mid)]

        
def test(algorithm, test_cases):
    for test in test_cases:
        attempt = algorithm(*test[0])
        if attempt != test[1]:
            print(f'Test failed\ninput: {test[0]}\nexpected: {test[1]}\ngot: {attempt}')

if __name__ == '__main__':
    test_cases = [
            (([1, 3], [2]), 2),
            (([1, 2], [3, 4]), 2.5),
            (([1, 3, 4], []), 3),
            (([5], [1, 4, 6, 8]), 5),
            (([], [12]), 12),
            (([2], []), 2),
            (([1, 2, 2], [1, 2, 3]), 2),
            (([1, 2, 4], [3, 5, 6]), 3.5),
    ]
    test(Solution().findMedianSortedArrays, test_cases)
