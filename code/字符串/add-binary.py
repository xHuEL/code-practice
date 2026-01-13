# 这一题有什么技巧？
# 当成当成常规的大数加法来做
class Solution:
    def add_c(self, a, b, carry) -> int:
        ia = ord(a) - ord('0')
        ib = ord(b) - ord('0')
        return ia + ib + carry

    def addBinary(self, a: str, b: str) -> str:
        m1 = len(a)
        m2 = len(b)

        n = max(m1, m2) + 1
        ans = [0] * n

        a = a[::-1]  # 反转字符串
        b = b[::-1]

        carry = 0  # 进位

        for i in range(n):
            ia = 0
            if i < m1:
                ia = ord(a[i]) - ord('0')

            ib = 0
            if i < m2:
                ib = ord(b[i]) - ord('0')

            c = ia + ib + carry
            ans[i] = int(c % 2)
            carry = c / 2

        # print(ans)
        res = ""
        if ans[n - 1] == 1:
            res += '1'

        for i in range(n - 2, -1, -1):
            res += str(ans[i])
        return res
