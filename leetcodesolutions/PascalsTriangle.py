#!/usr/bin/env python3
# PascalsTriangle.py
# Author : Shipra


class Solution:
    """
    Given an integer rowIndex, return the rowIndex-th (0-indexed) row
    of Pascal's triangle.
    """

    def getRow(self, rowIndex):
        rows = []

        for i in range(rowIndex + 1):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = rows[i - 1][j - 1] + rows[i - 1][j]
            rows.append(row)

        return rows[-1]


if __name__ == "__main__":
    print(Solution().getRow(5))
