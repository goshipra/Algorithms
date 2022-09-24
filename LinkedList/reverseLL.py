#!/usr/bin/env python3
# reverseLL.py
# Author : Shipra

class Node():
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def insertbegNode(self, data):
        if self.head is None:
            node = Node(data,self.head)
            self.head = node
            return

        node = Node(data,self.head)
        self.head.prev = node
        node.head = None


    def printascLL(self):
        if self.head is None:
            print("Linked list is Empty")
            return

        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next

    def printdecLL(self):
        if self.head is None:
            print("Linked list is Empty")
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        lastNode = itr

        itr2 = lastNode
        while itr2:
            print(itr.data)
            itr2 = itr2.prev


ll = LinkedList()
ll.insertbegNode(9)
ll.insertbegNode(3)
ll.insertbegNode(8)
ll.insertbegNode(5)
# ll.printascLL()
ll.printdecLL()
