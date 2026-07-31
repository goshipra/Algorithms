#!/usr/bin/env python3
# wordDistance.py
# Author : Shipra

# For example, given words = ["practice", "makes", "perfect", "coding",
# "makes"], word1 = "coding", word2 = "practice" -> 3.
# word1 = "makes", word2 = "coding" -> 1.


class Solution:
    """
    LeetCode 243. Given a list of words and two words word1 and word2,
    return the shortest distance between these two words in the list.
    """

    def shortestDistance(self, words, word1, word2):
        shortest = len(words)
        index1 = index2 = -1

        for i, word in enumerate(words):
            if word == word1:
                index1 = i
            elif word == word2:
                index2 = i

            if index1 != -1 and index2 != -1:
                shortest = min(shortest, abs(index1 - index2))

        return shortest


if __name__ == "__main__":
    words = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "coding"
    word2 = "practice"
    print(Solution().shortestDistance(words, word1, word2))
