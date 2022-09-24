#!/usr/bin/env python3
# mergeSortedList.py
# Author : Shipra

class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def makeLinkedList(self, list):
        for element in list:
            node = Node(element, self.head)
            self.head = node

    def printll(self):
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next

    def sort2list(self, list1, list2):
        if list1.head is None:
            return list2.head
        if list2.head is None:
            return list1.head

        if list1.head.data > list2.head.data:
            self.head = list1.head



ll = LinkedList()
sortedlist = [3, 2, 0]
ll.makeLinkedList(sortedlist)
# ll.printll()
ll2 = LinkedList()
sortedlist2 = [4, 2, 1]
ll2.makeLinkedList(sortedlist2)
# ll2.printll()
ll3 = LinkedList()
ll3.sort2list(ll, ll2)
