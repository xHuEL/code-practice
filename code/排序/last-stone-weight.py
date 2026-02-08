import heapq
from heapq import heappop, heappush
from typing import List


# 最大堆是一个可以自动维护最大值的数据结构
# 将最大堆中的最大值pop出来之后，最大堆会自动将剩余的最大值放在队列的前面
# 注意：最大堆只是维护最大值，最大堆是不知道第二大的数
# 在python中heapy来实现最大堆
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [-stone for stone in stones]
        heapq.heapify(arr)

        while len(arr) > 1:
            x = heappop(arr)
            y = heappop(arr)

            if x < y:
                heappush(arr, x - y)
            elif x > y:
                heappush(arr, y - x)
        return -arr[0] if arr else 0
