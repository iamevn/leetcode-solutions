#!/usr/bin/env python
"""Problem 23: Merge k Sorted Lists"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class PriorityQueue:  
    """a simple heap implementation of a priority queue
    by default uses identity for keys and <= for comparing keys"""
    def __init__(self, it=None, key=None, cmp=None):
        self._heap = []
        if not key:
            key = lambda a: a
        self._key = key
        if not cmp:
            cmp = lambda a, b: self._key(a) <= self._key(b)
        self._cmp = cmp
        
        if it is not None:
            for e in it:
                self.push(e)
    
    def __bool__(self):
        return bool(self._heap)
   
    def _children(self, idx):
        ret = (2 * idx + 1, 2 * idx + 2)
        if ret[0] >= len(self._heap):
            return (None, None)
        elif ret[1] >= len(self._heap):
            return (ret[0], None)
        else:
            return ret

    def _parent(self, idx):
        ret = (idx - 1) // 2
        if ret >= 0:
            return ret
        else:
            return None
    
    def push(self, e):
        h = self._heap
        key = self._key
        cmp = self._cmp
        h.append(e)
        idx = len(h) - 1
        while True:
            pidx = self._parent(idx)
            if pidx is None:  # at root
                break
            elif cmp(h[pidx], h[idx]):  # in place
                break
            else:
                h[pidx], h[idx] = h[idx], h[pidx]
                idx = pidx
        
    def pop(self):
        h = self._heap
        key = self._key
        cmp = self._cmp
        ret = h[0]
        
        if len(h) == 1:
            return h.pop()
        
        h[0] = h.pop()
        idx = 0
        while True:
            lidx, ridx = self._children(idx)
            if lidx is None:  # no children (tree is balanced)
                break
            elif ridx is None:  # one child with no children of its own
                if not cmp(h[idx], h[lidx]):
                    h[lidx], h[idx] = h[idx], h[lidx]
                break
            else:  # both children
                if cmp(h[idx], h[lidx]) and cmp(h[idx], h[ridx]):
                    break
                elif cmp(h[lidx], h[ridx]):
                    h[lidx], h[idx] = h[idx], h[lidx]
                    idx = lidx
                else:
                    h[ridx], h[idx] = h[idx], h[ridx]
                    idx = ridx
        return ret

    
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode

        merge k sorted lists containing n elements together into one list 
        this solution uses a minheap to find the minimum among the k lists

        building the minheap takes O(klogk) time and happens once
        popping the smallest element takes O(logk) time (n times)
        appending the extracted item to our new list takes O(1) time (n times)
        pushing the remaining list onto the heap takes O(logk) time (< n times)

        as we relink existing ListNodes together for form the resulting list,
          the only space overhead is local variables and variables local to
          the priority queue
        priority queue contains an array of ListNodes
        all other locals use constant space

        time complexity: O((k + n)logk)
        space complexity: O(k)
        """
        q = PriorityQueue(filter(lambda l: l is not None, lists),
                          key=lambda a: a.val)
        
        head = None
        tail = None
        while q:
            smallest = q.pop()
            if head is None:  # first item
                head = smallest
            else:
                tail.next = smallest

            tail = smallest

            if smallest.next:  # don't push empty lists onto heap
                q.push(smallest.next)

        return head
