from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = defaultdict(int)
        for word in words:
            counter[word] += 1

        sorted_list = sorted(counter.items(), key=lambda item: (-item[1], item[0]))
        return [item[0] for item in sorted_list][:k]


