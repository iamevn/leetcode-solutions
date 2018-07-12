#!/usr/bin/env python
from typing import List

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        """ Given matrix A, return transpose of A """
        row_len = len(A)
        col_len = len(A[0])
        if any(len(l) != col_len for l in A):
            raise ValueError('matrix not rectangular')

        return [[A[i][j] for i in range(row_len)] for j in range(col_len)]
