#!/usr/bin/env python3
# sortPeople2418.py
# Author : Shipra


class Solution:
    """
    Given names and heights of equal length where heights are distinct,
    return names sorted by height in descending order.
    """

    def sortPeople(self, names, heights):
        return [name for _, name in sorted(zip(heights, names), reverse=True)]


if __name__ == "__main__":
    names = ["Alice", "Bob", "Bob"]
    heights = [155, 185, 150]
    print(Solution().sortPeople(names, heights))
