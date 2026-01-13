from typing import List

# 可能实现有点复杂
# 查看v2版本
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        # k个数字之和

        m = 2 * n
        newCode = [0 for i in range(m)]
        sums = [0 for i in range(m)]
        # 重新赋值
        for i in range(m):
            if i < n:
                newCode[i] = code[i]
            else:
                newCode[i] = code[i - n]

        begin = 1
        end = 1
        sum1 = 0
        # print(newCode)
        for i in range(m - 1):
            if end - begin == abs(k):
                sums[begin - 1] = sum1
                if end >= m:
                    break

                sum1 -= newCode[begin]
                sum1 += newCode[end]
                begin += 1
                end += 1
            else:
                sum1 += newCode[end]
                end += 1
                # print(sum1)

        ans = [0 for _ in range(n)]
        if k > 0:
            for i in range(n):
                ans[i] = sums[i]
        else:
            for i in range(n):
                j = (i + k + n - 1) % n
                ans[i] = sums[j]
        return ans
