#!/usr/bin/env python3
# sortPeople2418.py
# Author : Shipra
#
class Solution(object):
    def sortPeople(self, names, heights):
        """
        better time and space complexity
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        dict = {}
        for i in range(0, len(names)):
            dict[heights[i]] = names[i]
        oplist = []
        heights.sort(reverse=True)
        for element in heights:
            oplist.append(dict[element])

        return oplist


class Solution(object):
    def sortPeople(self, names, heights):
        """
        high time and space complexity
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """

        sortedheight = sorted(heights,reverse=True)
        print(sortedheight)
        oplist = []
        for element in sortedheight:
            ind = heights.index(element)
            oplist.append(names[ind])

        return oplist


names = ["Alice", "Bob", "Bob"]
heights = [155, 185, 150]
obj = Solution()
obj.sortPeople(names, heights)
