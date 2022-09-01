#!/usr/bin/env python3
# ZigZag.py
# Author : Shipra

class Solution(object):
    def convert(self, s, numRows):
        """
        Zig zag conversion of "PAYPALISHIRING"

        P   A   H   N
        A P L S I I G
        Y   I   R


        P     I     N
        A   L S   I G
        Y  A  H  R
        P A   I f
        A     r

        numRows,numRows-2,numRows,numRows-2
        """


