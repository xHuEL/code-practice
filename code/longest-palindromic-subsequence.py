# https://leetcode.cn/problems/longest-palindromic-subsequence/description/?envType=problem-list-v2&envId=string
# 对于最长、最短子序列问题，一般都是使用动态规划

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        dp = [[0 for _ in s] for _ in s]
        for i in range(n):
            dp[i][i] = 1

        for i in range(1, n):
            if s[i] == s[i - 1]:
                dp[i - 1][i] = 2
            else:
                dp[i - 1][i] = 1

        for step in range(2, n):
            for l in range(n):
                r = l + step
                if r >= n:
                    continue

                dp[l][r] = max(dp[l + 1][r], dp[l][r])
                dp[l][r] = max(dp[l][r - 1], dp[l][r])
                if s[l] == s[r]:
                    dp[l][r] = max(dp[l + 1][r - 1] + 2, dp[l][r])

        return dp[0][n - 1]

