# 最长回文子串，有多种思路。
# 思路一: 最简单，按照


class Solution:
    def find_palindrome(self, s: str, l: int, r: int):
        result = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            result += 1
            l -= 1
            r += 1
        return result

    def longestPalindrome(self, s: str) -> str:
        str_len = len(s)
        if str_len <= 1:
            return s

        result_len = 0
        l = 0
        r = 0
        for i in range(str_len):
            odd_len = self.find_palindrome(s, i, i)
            even_len = self.find_palindrome(s, i, i + 1)
            if 2 * odd_len - 1 > result_len:
                result_len = 2 * odd_len - 1
                l = i - odd_len + 1
                r = i + odd_len - 1

            if even_len * 2 > result_len:
                result_len = 2 * even_len
                l = i - even_len + 1
                r = i + even_len

        return s[l: r + 1]


