#!/usr/bin/env python3
# mountain_array.py
# Author : Shipra


class Solution:
    """
    Determine whether the given array is a valid mountain array: it
    strictly increases to a single peak, then strictly decreases.
    """

    def validMountainArray(self, arr):
        n = len(arr)
        if n < 3:
            return False

        i = 0
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        if i == 0 or i == n - 1:
            return False

        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1

        return i == n - 1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(Solution().validMountainArray(arr))
