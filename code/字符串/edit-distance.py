## 最长公共子串，最长公共子序列，编辑距离
## 上面三种都是经典动态规划题目，但是仅仅限于两个字符串
## 多个字符串有别的实现方法
import sys


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)
        if len1 == 0 and len2 == 0:
            return 0
        if len1 == 0:
            return len2
        if len2 == 0:
            return len1

        dp = [[sys.maxsize] * (len2 + 1) for _ in range(len1 + 1)]
        dp[0][0] = 0
        for i in range(len1 + 1):
            dp[i][0] = i
        # 初始化第一行：从空串变成 word2 的前 j 个字符，需要 j 次插入操作。
        for j in range(len2 + 1):
            dp[0][j] = j

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j])

                # 所有的插入，替换，删除操作，都可以换算成dp[i - 1][j] + 1
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j])
                dp[i][j] = min(dp[i][j - 1] + 1, dp[i][j])
                dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i][j])

        return dp[len1][len2]
