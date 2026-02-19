from collections import Counter
from typing import List


# 思路：前缀和
# 数组为a[0], a[1], a[2], a[3], a[4]
# 那么前缀和sums[0] = a[0], sums[1] = a[0] + a[1] = sums[0] + a[1], sums[2] = sums[1] + a[2]
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sums = [nums[i] for i in range(n)]
        for i in range(n):
            if i > 0:
                sums[i] += sums[i - 1]

        counter = Counter()
        ans = 0
        # 使用计数器保存当前所有前缀和
        # 对于当前遍历的位置i，前缀和为sums[i]， 假如当前位置为子数组的结束位置，找到sums[i] - sums[j] = k 开始位置j的个数，加进最后的结果
        counter[0] = 1
        for i in range(n):
            left = sums[i] - k
            ans += counter[left]
            counter[sums[i]] += 1

        return ans
