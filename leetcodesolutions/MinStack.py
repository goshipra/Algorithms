#!/usr/bin/env python3
# MinStack.py
# Author : Shipra


class MinStack:
    """
    Design a stack that supports push, pop, top, and retrieving the
    minimum element, all in constant time.
    """

    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.stack:
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.stack:
            return min(self.stack)


if __name__ == "__main__":
    obj = MinStack()
    obj.push(3)
    obj.push(4)
    obj.push(2)
    obj.push(5)
    obj.pop()
    print(obj.getMin())
    print(obj.top())
