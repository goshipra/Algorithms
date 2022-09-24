#!/usr/bin/env python3
# PascalsTriangle.py
# Author : Shipra

class Solution(object):
    def getRow(self, rowIndex):
        """
        Implementing Pascals Triangle
        """
        ResultList = []

        for i in range(0, rowIndex+1):
            row = []

            if i == 0:
                row.append(1)
            else:
                row.insert(0, 1)
                row.insert(i, 1)

                for j in range(1, i):
                    leftabove = ResultList[i - 1][j - 1]
                    rightabove = ResultList[i - 1][j]
                    row.insert(j, leftabove + rightabove)

            ResultList.append(row)

        return ResultList[-1]


obj = Solution()
print(obj.getRow(3))
