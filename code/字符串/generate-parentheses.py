# 很明显递归来解决
# 没有技巧，都是经验
# 但是从n <= 8 其实就知道，使用递归来实现
from typing import List


class Solution:
    def generate(self, l : int, r : int, s : str, res : List[str]):
        if l == 0 and r == 0:
            res.append(s)

        if l > 0:
            new_s = s + '('
            self.generate(l - 1, r, new_s, res)
        if r > 0 and l < r:
            new_s = s + ')'
            self.generate(l, r - 1, new_s, res)


    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.generate(n, n, "", res)
        return res