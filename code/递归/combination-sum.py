from typing import List


class Solution:
    # num是当前遍历到candidates的位置
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start, curSum, path):
            if curSum == target:
                result.append(path[:])
                return

            if curSum > target:
                return

            for i in range(start, len(candidates)):
                # 剪枝
                if curSum + candidates[i] > target:
                    return

                path.append(candidates[i])
                dfs(i, curSum + candidates[i], path)
                path.pop()

        result = []
        candidates.sort()
        dfs(0, 0, [])
        return result
