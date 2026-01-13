import sys
from typing import List

## 考虑时间复杂度：一百万次计算为1s
## trie构建时间为O(n), 其中n最大为5*10^4 * 8
## trie遍历时间为O(n), 其中n最大为5 * 10 ^ 4 * 8
## trie树的工作原理：https://oi-wiki.org/string/trie/#__tabbed_1_2

class Node:
    def __init__(self):
        self.end = False
        self.cnt = 0
        self.next = {}

class Trie:
    def __init__(self):
        self.root = Node()

    def append(self, string : str):
        cur = self.root
        for s in string:
            if cur.next.__contains__(s):
                cur = cur.next[s]
            else:
                newNode = Node()
                cur.next[s] = newNode
                cur = newNode
        cur.cnt += 1
        cur.end = True

    def find(self, string : str) -> int:
        cur = self.root
        result = 0
        for s in string:
            if cur.next.__contains__(s):
                result += 1
                cur = cur.next[s]
            else:
                break
        return result

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        for element in arr1:
            string = str(element)
            trie.append(string)

        result = 0
        for element in arr2:
            string = str(element)
            result = max(trie.find(string), result)
        return result








