class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)

        ans = 0
        i = 0
        while i < n and s[i] == ' ':
            i += 1
            # print(i)

        sign = True
        if i < n and s[i] == '-':
            sign = False
            i += 1
        elif i < n and s[i] == '+':
            sign = True
            i += 1

        while i < n and '0' <= s[i] <= '9':
            ans = ans * 10 + int(s[i])
            i += 1

        if sign:
            if ans > 2 ** 31 - 1:
                return 2 ** 31 - 1
            return ans
        else:
            if ans > 2 ** 31:
                return -2 ** 31
            return -ans


