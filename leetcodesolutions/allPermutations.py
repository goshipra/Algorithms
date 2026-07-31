#!/usr/bin/env python3
# allPermutations.py
# Author : Shipra


def permute(s, prefix=""):
    """Print all permutations of string s."""
    if not s:
        print(prefix, end="  ")
        return

    for i in range(len(s)):
        rest = s[:i] + s[i + 1:]
        permute(rest, prefix + s[i])


if __name__ == "__main__":
    s = "ABC"
    print("All possible strings are:")
    permute(s)
