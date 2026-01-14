from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 异位词，使用python的counter, 后面会用到
        counter = Counter()
        for c in s:
            counter[c] += 1

        for c in t:
            if counter[c] == 0:
                return False
            counter[c] -= 1
            if counter[c] == 0:
                del counter[c]

        if len(counter) != 0:
            return False
        return True
