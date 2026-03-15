from collections import defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = defaultdict(int)

        for c in s:
            counter[c] += 1

        sorted_list = sorted(counter.items(), key=lambda item: (-item[1], item[0]))
        ans = []
        for key, value in sorted_list:
            for i in range(value):
                ans.append(key)
        return "".join(ans)
