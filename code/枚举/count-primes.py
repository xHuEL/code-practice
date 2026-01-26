# 很经典的质数求解方法
class Solution:
    def countPrimes(self, n: int) -> int:
        # 质数求解方法，筛法
        ans = [0 for _ in range(n + 1)]
        cnt = 0
        for i in range(n + 1):
            if ans[i] == 1:
                continue

            j = 2
            cnt += 1
            while j * i <= n:
                ans[j * i] = 1

        return cnt
