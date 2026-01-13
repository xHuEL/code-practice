# 这个题目应该是可以使用str的split函数来实现的
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s_list = s.split(" ")
        n = len(s_list)
        return len(s_list[n - 1])
