from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []

        n = len(s)
        m = len(p)

        if m > n:
            return []

        counter = Counter()

        ll = 0
        r = m - 1

        for i in range(ll, r + 1):
            counter[s[i]] += 1

        for c in p:
            counter[c] -= 1
            if counter[c] == 0:
                del counter[c]

        if len(counter) == 0:
            ans.append(0)

        while r < n - 1:
            ll = ll + 1
            r = r + 1
            counter[s[ll - 1]] -= 1
            if counter[s[ll - 1]] == 0:
                del counter[s[ll - 1]]

            counter[s[r]] += 1
            if counter[s[r]] == 0:
                del counter[s[r]]

            if len(counter) == 0:
                ans.append(ll)

        return ans
