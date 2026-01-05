class Solution:
    def find_palindrome(self, s: str, l: int, r: int) -> int:
        result = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            result += 1
            l -= 1
            r += 1
        return result

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(1, n):
            ans += self.find_palindrome(s, i - 1, i)

        for i in range(n):
            ans += self.find_palindrome(s, i, i)
        return ans