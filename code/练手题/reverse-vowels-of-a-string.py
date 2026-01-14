class Solution:
    def isYuan(self, c):
        str = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        if c in str:
            return True
        return False

    def reverseVowels(self, s: str) -> str:
        n = len(s)

        ll = 0
        rr = n - 1
        ans = ['0' for _ in range(n)]

        while ll <= rr:
            if not self.isYuan(s[ll]):
                ans[ll] = s[ll]
                ll += 1
                continue

            if not self.isYuan(s[rr]):
                ans[rr] = s[rr]
                rr -= 1
                continue

            ans[ll], ans[rr] = s[rr], s[ll]
            ll += 1
            rr -= 1
        return ''.join(ans)
