class Solution:


    def climbStairs(self, n: int) -> int:
        f = [0 for _ in range(n)]
        f[1] = 1
        f[2] = 1

        for i in range(3, n + 1):
            f[i] = f[i - 1] + f[i - 2]

        return f[n]


    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        if n == 2:
            return 1

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

