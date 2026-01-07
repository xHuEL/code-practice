from typing import List

from typing import List
from collections import defaultdict

## 多项式hash
class Hasher:
    def __init__(self, s: str):
        self.M = 233
        self.N = 10000007
        self.L = 10
        self.hash_val = 0
        self.M_power = pow(self.M, self.L - 1, self.N)

        for c in s:
            self.hash_val = (self.hash_val * self.M + ord(c)) % self.N

    def roll(self, old_char: str, new_char: str):
        self.hash_val = (
            (self.hash_val - ord(old_char) * self.M_power) * self.M
            + ord(new_char)
        ) % self.N

    def value(self):
        return self.hash_val


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 10:
            return []

        hasher = Hasher(s[:10])

        # hash -> set of sequences
        bucket = defaultdict(set)
        # sequence -> count
        seen = defaultdict(int)

        first = s[:10]
        bucket[hasher.value()].add(first)
        seen[first] = 1

        ans = []

        for i in range(10, n):
            hasher.roll(s[i - 10], s[i])
            seq = s[i - 9:i + 1]
            h = hasher.value()

            # 精确判重
            if seq in bucket[h]:
                seen[seq] += 1
                if seen[seq] == 2:
                    ans.append(seq)
            else:
                bucket[h].add(seq)
                seen[seq] = 1

        return ans






