#!/usr/bin/env python3
# doublylinkedlist.py
# Author : Shipra


class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class DoublyLL:
    def __init__(self, head=None):
        self.head = head

    def insertBeginning(self, data):
        node = Node(None, data, self.head)
        if self.head is not None:
            self.head.prev = node
        self.head = node

    def insertEnd(self, data):
        if self.head is None:
            self.insertBeginning(data)
            return
        itr = self.getLastnode()
        node = Node(itr, data, None)
        itr.next = node

    def NewList(self, newlist):
        for data in reversed(newlist):
            self.insertBeginning(data)

    def listlength(self):
        counter = 0
        itr = self.head
        while itr:
            counter += 1
            itr = itr.next
        return counter

    def printllforward(self):
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next

    def getLastnode(self):
        itr = self.head
        while itr and itr.next:
            itr = itr.next
        return itr

    def printllbackward(self):
        itr = self.getLastnode()
        while itr:
            print(itr.data)
            itr = itr.prev


if __name__ == "__main__":
    doublelist = DoublyLL()
    doublelist.insertBeginning(9)
    doublelist.insertBeginning(8)
    doublelist.insertBeginning(6)
    doublelist.printllforward()
    doublelist.printllbackward()
