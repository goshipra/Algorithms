#!/usr/bin/env python3
# mergeSortedArray.py
# Author : Shipra


class Solution:
    """
    nums1 and nums2 are sorted arrays; nums1 has length m + n, with the
    last n elements set to 0. Merge nums2 into nums1 in place as one
    sorted array of length m + n.
    """

    def merge(self, nums1, m, nums2, n):
        i, j, k = m - 1, n - 1, m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1)
