class Solution:
    def isyuan(self, c):
        ss = ['a', 'e', 'i', 'o', 'u']
        for cc in ss:
            if cc == c:
                return True
        return False

    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)

        ll = 0
        rr = min(n, ll + k)
        cnt = 0
        for i in range(ll, rr):
            if self.isyuan(s[i]):
                cnt += 1

        ans = cnt
        while rr < n:
            ll += 1
            rr += 1

            cnt -= self.isyuan(s[ll - 1])
            cnt += self.isyuan(s[rr - 1])

            if cnt > ans:
                ans = cnt

        return ans

