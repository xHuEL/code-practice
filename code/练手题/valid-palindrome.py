class Solution:
    def isOK(self, c):
        if '0' <= c <= '9':
            return True

        if 'a' <= c <= 'z':
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        n = len(s)

        # 双指针
        ll = 0
        rr = n - 1
        while ll < rr:
            if not self.isOK(s[ll]):
                ll = ll + 1
                continue

            if not self.isOK(s[rr]):
                rr = rr - 1
                continue

            if s[ll] != s[rr]:
                return False

            ll = ll + 1
            rr = rr - 1

        return True
