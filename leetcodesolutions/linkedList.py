#!/usr/bin/env python3
# linkedList.py
# Author : Shipra

class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def insertBeginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insertEnd(self, data):
        if self.head is None:
            self.insertBeginning(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        node = Node(data, None)
        itr.next = node

    def NewList(self, newlist):
        i = len(newlist) - 1
        while i >= 0:
            self.insertBeginning(newlist[i])
            i -= 1

    def listlength(self):
        counter = 1
        itr = self.head
        while itr.next:
            counter += 1
            itr = itr.next
        return counter

    def removebyindex(self, index):
        if index < 0 or index >= self.listlength():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insertIndex(self, index, data):
        if index < 0 or index > self.listlength():
            raise Exception("Invalid Index")

        if index == 0:
            self.insertBeginning(data)
            return

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insertByValue(self, value ,data):

        if self.head == None:
            return

        if self.head.data == value:
            node = Node(data, self.head.next)
            return

        itr = self.head
        while itr.next:
            if itr.data == value:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next

    def removeByValue(self, value):

        if self.head == None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == value:
                itr.next = itr.next.next
                break
            itr = itr.next

    def lprint(self):
        if self.head == None:
            return

        itr = self.head

        while itr:
            print(itr.data)
            itr = itr.next


newList = LinkedList()
newList.lprint()
newList.insertBeginning(8)
newList.insertBeginning(10)
newList.insertEnd(9)
list = [5, 4, 3, 2, 1]
newList.NewList(list)
newList.listlength()
newList.removebyindex(0)
newList.insertIndex(4, 89)
newList.removeByValue(89)
newList.insertByValue(10,90)
newList.lprint()
