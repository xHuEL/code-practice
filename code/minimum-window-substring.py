# https://leetcode.cn/problems/minimum-window-substring/description/?envType=problem-list-v2&envId=string
## 滑动窗口，我也是看题解的。。。

import sys


class Solution:
    def __init__(self):
        self.ori = {}
        self.cnt = {}

    def check(self) -> bool:
        for key, val in self.ori.items():
            if self.cnt.__contains__(key):
                if self.ori[key] > self.cnt[key]:
                    return False
            else:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0

        s_len = len(s)
        ans = sys.maxsize
        ans_str = ""

        for c in t:
            if self.ori.__contains__(c):
                self.ori[c] += 1
            else:
                self.ori[c] = 1

        while r < s_len:
            if self.ori.__contains__(s[r]):
                if not self.cnt.__contains__(s[r]):
                    self.cnt[s[r]] = 1
                else:
                    self.cnt[s[r]] += 1

            r += 1

            ## 判断
            while self.check() and l <= r:
                if r - l + 1 < ans:
                    ans = r - l + 1
                    ans_str = s[l: r]

                if self.cnt.__contains__(s[l]):
                    self.cnt[s[l]] -= 1

                l += 1

        return ans_str










