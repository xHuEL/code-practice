# 滑动窗口
# 思路参考: https://leetcode.cn/problems/substring-with-concatenation-of-all-words/?envType=problem-list-v2&envId=string
from collections import Counter
from typing import List


class Solution:
    def findSubStringByWindow(self, s: str, l1: int, r: int, words: List[str], maps: dict) -> List[int]:
        ans = []
        if maps.__contains__(l1):
            return ans
        maps[l1] = 1

        differ = Counter()
        m = len(words[0])  # 子字符串的长度
        n = len(s)  # 原始字符串的长度

        if n < m:
            return []

        # 统计[l, r) 是否包含words字符串列表
        for ll in range(l1, r, m):
            word = s[ll: ll + m]
            differ[word] += 1

        for word in words:
            differ[word] -= 1
            if differ[word] == 0:
                del differ[word]

        # print(maps)
        # print(differ)

        if len(differ) == 0:
            ans.append(l1)

        # 滑动窗口统计 [ll, rr)是否包含words字符串列表，其中[ll, rr)是[l, r)移m，2m，3m....等长度得到的区间
        # 也就是统计[l + m, r + m), [l + 2 * m, r + 2 * m).....这些区间是否包含words字符串列表
        while r < n:
            left_word = s[l1: l1 + m]
            right_word = s[r: r + m]

            l1 += m
            r += m

            if maps.__contains__(l1):
                continue
            maps[l1] = 1

            differ[left_word] -= 1
            if differ[left_word] == 0:
                del differ[left_word]

            differ[right_word] += 1
            if differ[right_word] == 0:
                del differ[right_word]

            # print(differ)
            if len(differ) == 0:
                ans.append(l1)

        return ans

    def findSubstring(self, string: str, words: List[str]) -> List[int]:
        n = len(string)
        m = len(words[0])
        s = len(words)  # 子字符串列表

        if m > n:
            return []

        ans = []
        maps = {}
        for i in range(0, n, 1):
            ll = i
            r = i + m * s

            if r > n:
                break

            res = self.findSubStringByWindow(string, ll, r, words, maps)
            ans.extend(res)

        return ans


