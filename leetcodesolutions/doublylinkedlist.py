#!/usr/bin/env python3
# doublylinkedlist.py
# Author : Shipra

class Node():
    def __init__(self,prev=None, data=None, next=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLL():
    def __init__(self,head=None):
        self.head = head


    def insertBeginning(self, data):
        if self.head == None:
            node = Node(None,data,self.head)
            self.head = node
        else:
            node = Node(None,data, self.head)
            self.head = node
            self.head.prev = node

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




    def printllforward(self):
        if self.head == None:
            return

        itr = self.head

        while itr:
            print(itr.data)
            itr = itr.next

    def getLastnode(self):
        itr = self.head

        while itr.next:
            itr = itr.next
        return itr



    def printllbackward(self):
        if self.head == None:
            return

        itr = self.getLastnode()

        while itr:
            print(itr.data)
            itr = itr.prev


doublelist = DoublyLL()
doublelist.insertBeginning(9)
doublelist.insertBeginning(8)
doublelist.insertBeginning(6)
doublelist.printllforward()
doublelist.printllbackward()








