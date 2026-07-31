#!/usr/bin/env python3
# mergeLinkedList.py
# Author : Shipra


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Merge two sorted linked lists and return it as a sorted list.
    """

    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2
        return dummy.next


def build_list(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(node):
    values = []
    while node:
        values.append(node.val)
        node = node.next
    return values


if __name__ == "__main__":
    list1 = build_list([1, 2, 4])
    list2 = build_list([1, 3, 4])
    merged = Solution().mergeTwoLists(list1, list2)
    print(to_list(merged))
