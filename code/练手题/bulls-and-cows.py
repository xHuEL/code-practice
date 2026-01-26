class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        maps = [0 for _ in range(10)]
        maps2 = [0 for _ in range(10)]

        bulls = 0
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                maps[int(g)] += 1
                maps2[int(s)] += 1

        cows = sum(min(s, g) for s, g in zip(maps2, maps))
        return f'{bulls}A{cows}B'