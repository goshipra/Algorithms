#!/usr/bin/env python3
# ZigZag.py
# Author : Shipra


class Solution:
    """
    Zig-zag conversion of a string across numRows, read row by row.
    Example: "PAYPALISHIRING" with numRows=3 ->
        P   A   H   N
        A P L S I I G
        Y   I   R
    read row by row: "PAHNAPLSIIGYIR"
    """

    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        current_row = 0
        going_down = False

        for ch in s:
            rows[current_row] += ch
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1

        return "".join(rows)


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3
    print(Solution().convert(s, numRows))
