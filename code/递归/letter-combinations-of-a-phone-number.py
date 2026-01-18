from typing import List

maps = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
class Solution:
    def dfs(self, digits: str, num: int, s: str, ans : List[str]):
        if num >= len(digits):
            ans.append(s)
            return

        cur_digit = int(digits[num])
        map_str = maps[cur_digit]
        for c in map_str:
            new_s = s + c
            self.dfs(digits, num + 1, new_s, ans)


    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        self.dfs(digits, 0, "", ans)
        return ans


