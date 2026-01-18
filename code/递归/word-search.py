from typing import List

dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def isInBoard(x, y):
            if 0 <= x < m and 0 <= y < n:
                return True

            return False

        def dfs(x: int, y: int, num: int, path: List[str]) -> bool:
            # print(path)
            if num == len(word):
                return True

            for j in range(4):
                newX = x + dir[j][0]
                newY = y + dir[j][1]

                if not isInBoard(newX, newY):
                    continue

                if visited[newX][newY] == 1:
                    continue

                if board[newX][newY] != word[num]:
                    continue

                visited[newX][newY] = 1
                path.append(board[newX][newY])
                if dfs(newX, newY, num + 1, path):
                    return True
                path.pop()
                visited[newX][newY] = 0

            return False

        m = len(board)
        n = len(board[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited[i][j] = 1
                    path = [board[i][j]]
                    if dfs(i, j, 1, path):
                        return True
                    path.pop()
                    visited[i][j] = 0

        return False
