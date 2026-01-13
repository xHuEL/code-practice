# 统计 + 序列，动态规划
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # 初始化
        for i in range(m + 1):
            for j in range(n + 1):
                dp[i][j] = 0

        dp[0][0] = 1

        for j in range(n + 1):  # 表示t[0:i]
            for i in range(m + 1):  # 统计出现在s[0:j]次数
                if j > i:
                    continue

                dp[i][j] += dp[i - 1][j]
                if t[j - 1] == s[i - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[m][n]

