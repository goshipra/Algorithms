#!/usr/bin/env python3
# BST.py
# Author : Shipra


class BST:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def insertNode(self, data):
        if self.data is None:
            self.data = data
            return

        if self.data > data:
            if self.lchild is None:
                self.lchild = BST(data)
            else:
                self.lchild.insertNode(data)
        else:
            if self.rchild is None:
                self.rchild = BST(data)
            else:
                self.rchild.insertNode(data)

    def searchNode(self, data):
        if self.data is None:
            print("Empty Tree")
            return
        if self.data == data:
            print("Found it ")
            return
        if self.data > data:
            if self.lchild is None:
                print("Not Found")
                return
            else:
                self.lchild.searchNode(data)
        else:
            if self.rchild is None:
                print("Not Found")
                return
            else:
                self.rchild.searchNode(data)

    def inordertrav(self):
        if self.data is None:
            print("Tree is Empty")
            return
        if self.lchild:
            self.lchild.inordertrav()
        print(self.data,end="->")
        if self.rchild:
            self.rchild.inordertrav()

    def preordertrav(self):
        if self.data is None:
            print("Tree is Empty")
            return
        print(self.data,end="->")
        if self.lchild:
            self.lchild.preordertrav()
        if self.rchild:
            self.rchild.preordertrav()

    def postordertrav(self):
        if self.data is None:
            print("Tree is Empty")
            return
        if self.lchild:
            self.lchild.postordertrav()
        if self.rchild:
            self.rchild.postordertrav()
        print(self.data,end="->")

    def deletion(self,data):

        if self.data is None:
            print("Tree is Empty")

        if data > self.data:
            if self.rchild:
                self.rchild = self.rchild.deletion(data)
            else:
                print("Node Does not Exist")
        elif data < self.data:
            if self.lchild:
                self.lchild = self.lchild.deletion(data)
            else:
                print("Node Does not Exist")
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            node = self.rchild
            while self.lchild:
                node = node.lchild
            self.data = node.data
            self.rchild = self.rchild.deletion(node.data)
        return self


root = BST(None)
InputList = [7, 6, 8, 5, 1, 2, 9, 15, 10, 4]
for data in InputList:
    root.insertNode(data)

# root.searchNode(15)
# root.searchNode(9)
print("InOrder : ")
root.inordertrav()
print("")
print("PreOrder : ")
root.preordertrav()
print("")
print("PostOrder : ")
root.postordertrav()
print("")
print("deletion of 10")
root.deletion(10)
root.inordertrav()

