#!/usr/bin/env python3
# boat.py
# Author : Shipra

# You are given an array people where people[i] is the weight of the ith
# person, and an infinite number of boats where each boat can carry a
# maximum weight of limit. Each boat carries at most two people at the
# same time, provided the sum of the weight of those people is at most
# limit. Return the minimum number of boats to carry every given person.


class Solution:
    """
    Rescue boat algorithm: minimum boats needed given a max weight limit
    per boat and the weight of each person to be rescued.
    """

    def numRescueBoats(self, people, limit):
        people.sort()
        left, right = 0, len(people) - 1
        count = 0

        while left <= right:
            if people[right] + people[left] <= limit:
                left += 1
            right -= 1
            count += 1

        return count


if __name__ == "__main__":
    people = [1, 2, 2, 3]
    print(Solution().numRescueBoats(people, limit=3))
