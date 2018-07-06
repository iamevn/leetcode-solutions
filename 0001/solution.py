#!/usr/bin/env python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # list of tuples: (index into nums, num at that index)
        idxmap = [(i, nums[i]) for i in range(len(nums))]
        # list sorted by number value
        sorted_nums = sorted(idxmap, key=lambda e: e[1])


        def idx_sum(*args):
            'for each argument index into sorted_nums, sum up the number value from that index'
            sum = 0
            for arg in args:
                sum += sorted_nums[arg][1]
            return sum
        
        for a in range(len(sorted_nums) - 1):
            for b in range(a + 1, len(nums)):
                if idx_sum(a, b) < target:
                    continue
                elif idx_sum(a, b) == target:
                    return [sorted_nums[e][0] for e in (a, b)]
                else: # idx_sum(a, b) > target
                    break

    def better(self, nums, target):
        mapidx = {}

        for idx in range(len(nums)):
            val = nums[idx]
            if target - val in mapidx:
                return [mapidx[target - val], idx]
            else:
                mapidx[val] = idx

def test():
    s = Solution()
    tests = [
            (([3, 2, 4], 6),
                [1, 2]),
            (([3, 3], 6),
                [0, 1]),
            ]
    for test in tests:
        attempt = s.better(*test[0])
        if attempt != test[1]:
            print(f'Test failed\ninput: {test[0]}\nexpected: {test[1]}\ngot: {attempt}')

if __name__ == '__main__':
    test()
