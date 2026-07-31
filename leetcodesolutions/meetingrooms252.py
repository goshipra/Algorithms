#!/usr/bin/env python3
# meetingrooms252.py
# Author : Shipra

# Example 1:
# Input: [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:
# Input: [[7,10],[2,4]]
# Output: true


class Solution:
    """
    Given an array of meeting time intervals [[s1,e1],[s2,e2],...]
    (si < ei), determine if a person could attend all meetings.
    """

    def meetingRooms(self, intervals):
        sorted_intervals = sorted(intervals)
        for i in range(len(sorted_intervals) - 1):
            if sorted_intervals[i][1] > sorted_intervals[i + 1][0]:
                return False
        return True


if __name__ == "__main__":
    intervals = [[0, 30], [5, 10], [15, 20]]
    print(Solution().meetingRooms(intervals))
