from typing import List


class StrHasher:
    def __init__(self, s: str):
        self.s = s
        self.hash = [0] * 26
        for c in s:
            self.hash[ord(c) - ord('a')] += 1

        self.hash_value = tuple(self.hash)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = dict()
        for s in strs:
            hasher = StrHasher(s)
            hash_val = hasher.hash_value
            if hash_map.__contains__(hash_val):
                hash_val_list = hash_map[hash_val]
                hash_val_list.append(s)
                hash_map[hash_val] = hash_val_list
            else:
                hash_map[hash_val] = [s]

        ans = []
        for value in hash_map.values():
            ans.append(value)
        return ans
