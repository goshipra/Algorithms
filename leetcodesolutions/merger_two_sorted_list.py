#!/usr/bin/env python3
# merger_two_sorted_list.py
# Author : Shipra


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next


def list_input():
    """Take numbers as user input and build a list of ints."""
    values = []
    value = None
    while value != "":
        value = input("Enter the value to create a list: ")
        if value != "":
            values.append(int(value))
    return values


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.head = Node(1)
    val1 = Node(2)
    val2 = Node(3)
    linked_list.head.next = val1
    val1.next = val2

    linked_list.printlist()

    for i in range(2):
        values = list_input()
        print("List" + str(i) + "= ", values)
