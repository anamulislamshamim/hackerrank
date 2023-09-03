#!/usr/bin/env python3

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#
class Node:
    def __init__(self):
        self.children = {}
        self.is_complete = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        temp = self.root
        w_len = len(word)
        sub = ""
        for char in word:
            # if char already exist in trie then just add it to the substring
            if temp.children.get(char):
                sub += char
            # check wheter the prefix is completed in trie or the prefix
            if temp.is_complete or len(sub) == w_len:
                # print(temp.is_complete, sub, word)
                return True
            # print(temp.is_complete, sub, word)
            if not temp.children.get(char):
                temp.children[char] = Node()
            temp = temp.children[char]
        temp.is_complete = True
        return False


def noPrefix(words):
    # Write your code here
    trie = Trie()
    for word in words:
        if trie.insert(word):
            print('BAD SET')
            print(word)
            return
    print('GOOD SET')

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
