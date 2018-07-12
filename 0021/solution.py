# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        "merge lists l1 and l2 and return the sorted list"
        
        merged = ListNode(0)  # dummy head node
        prev = merged
        
        while l1 and l2:
            if l1.val < l2.val:
                tmp = l1
                l1 = l1.next
            else:
                tmp = l2
                l2 = l2.next
            prev.next = tmp
            prev = prev.next
        
        if l1:
            prev.next = l1
        elif l2:
            prev.next = l2
                
        return merged.next
