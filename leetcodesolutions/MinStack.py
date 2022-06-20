#!/usr/bin/env python3
# MinStack.py
# Author : Shipra


class MinStack(object):
    '''
    Design a stack that supports push, pop, top, and
    retrieving the minimum element in constant time.

    Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.
    '''

    def __init__(self):
        self.stack = []

    def push(self, val):
        if val is not None:
            self.stack.append(val)

    def pop(self):
        if len(self.stack) != 0:
            self.stack.pop()

    def top(self):
        if len(self.stack) != 0:
            return self.stack[-1]

    def getMin(self):
        if len(self.stack) != 0:
            return min(self.stack)



obj = MinStack()

print(obj.getMin())


