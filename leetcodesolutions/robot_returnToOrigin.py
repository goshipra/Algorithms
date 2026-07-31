#!/usr/bin/env python3
# robot_returnToOrigin.py
# Author : Shipra


class Solution:
    """
    A robot starts at (0, 0) and moves according to a string of moves
    made up of 'R', 'L', 'U', 'D'. Return True if it ends up back at
    the origin.
    """

    def judgeCircle(self, moves):
        x = y = 0
        for move in moves:
            if move == "R":
                x += 1
            elif move == "L":
                x -= 1
            elif move == "U":
                y += 1
            elif move == "D":
                y -= 1
        return x == 0 and y == 0


if __name__ == "__main__":
    moves = "ULL"
    print(Solution().judgeCircle(moves))
