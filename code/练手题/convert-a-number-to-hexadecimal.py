class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        maps = '0123456789abcdef'
        if num < 0:
            num += 2 ** 32

        ans = ''
        while num > 0:
            inx = int(num % 16)
            c = maps[inx]
            ans += c
            num = int(num / 16)
        return ans[::-1]