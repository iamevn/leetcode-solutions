#!/usr/bin/env python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: 'TreeNode') -> 'TreeNode':
        max_depth = 0
        deepest_nodes = {root}
        nodelist = [(root, 0)]  # list of (node, depth) tuples
        reverse_edges = {root: None}

        # find deepest nodes
        while nodelist:
            (head, depth) = nodelist.pop()
            if depth == max_depth:
                deepest_nodes.add(head)
            elif depth > max_depth:
                max_depth = depth
                deepest_nodes = {head}

            for node in head.left, head.right:
                if node is not None:
                    nodelist.append((node, depth + 1))
                    reverse_edges[node] = head

        # find common parent
        if len(deepest_nodes) == 1:
            return deepest_nodes.pop()
        parents = {reverse_edges[node] for node in deepest_nodes}
        while len(parents) > 1:
            # len(parents) will remain >= 1 because of tree structure
            parents = {reverse_edges[node] for node in parents}

        return parents.pop()
