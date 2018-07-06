#!/usr/bin/env python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        if type(other) != ListNode:
            return False

        return self.val == other.val and self.next == other.next

    def __repr__(self):
        if self.next is None:
            return f'{self.val}'
        else:
            return f'{self.val} -> {self.next}'


def build_list(iterable):
    next_node = None
    for e in reversed(iterable):
        node = ListNode(e)
        node.next, next_node = next_node, node
    return next_node

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first_node = None
        carry = 0
        prev = None
        while l1 is not None or l2 is not None or carry != 0:
            if l1 is None:
                l1 = ListNode(0)
            if l2 is None:
                l2 = ListNode(0)

            new_val = l1.val + l2.val + carry
            if new_val > 9:
                new_val -= 10
                carry = 1
            else:
                carry = 0

            new_node = ListNode(new_val)

            if first_node is None:
                first_node = new_node
            else:
                prev.next = new_node

            prev = new_node
            l1 = l1.next
            l2 = l2.next
        
        return first_node
        
def test():
    s = Solution()
    tests = [
            (([2, 4, 3], [5, 6, 4]), [7, 0, 8]),
            (([2, 4, 3], [5, 9]), [7, 3, 4]),
            (([4, 3], [5, 9, 1]), [9, 2, 2]),
            (([5], [6]), [1, 1]),
    ]
    tests = [((build_list(l1), build_list(l2)), build_list(sol)) for ((l1, l2), sol) in tests]

    for test in tests:
        attempt = s.addTwoNumbers(*test[0])
        if attempt != test[1]:
            print(f'Test failed\ninput: {test[0]}\nexpected: {test[1]}\ngot: {attempt}')

if __name__ == '__main__':
    test()
