#!/usr/bin/env python3
# mergeLinkedList.py
# Author : Shipra

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = None

        while list1 and list2:





list1 = [1,2,4]
list2 = [1,3,4]
mergedList = Solution()
print(mergedList.mergeTwoLists(list1,list2))
