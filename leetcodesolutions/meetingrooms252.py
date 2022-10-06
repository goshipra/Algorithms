#!/usr/bin/env python3
# meetingrooms252.py
# Author : Shipra

# Example 1:
#
# Input: [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:
#
# Input: [[7,10],[2,4]]
# Output: true

class Solution():
    def meetingRooms(self, InputTimes):
        """
        Given an array of meeting time intervals consisting of start and end times
         [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

        """
        sortedTimes = sorted(InputTimes)
        for i in range(len(InputTimes)-1):
            print(sortedTimes[i])
            if sortedTimes[i][1] > sortedTimes[i+1][0]:
                return False
        return True


Input = [[0, 30], [5, 10], [15, 20]]
decision = Solution()
print(decision.meetingRooms(Input))
