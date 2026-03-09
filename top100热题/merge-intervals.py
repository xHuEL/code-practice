from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_data = sorted(intervals, key=lambda x: (x[0], x[1]))

        def merge(intervals1, intervals2):
            return [intervals1[0], max(intervals2[1], intervals1[1])]

        ans = []
        for [left, right] in sorted_data:
            if len(ans) == 0:
                ans.append([left, right])
            else:
                top = ans[-1]
                if top[1] < left:
                    ans.append([left, right])
                else:
                    ans.pop(-1)
                    ans.append(merge(top, [left, right]))

        return ans

