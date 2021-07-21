import unittest
import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def solution(n, arrays):
    def dfs(x, y):
        if x < 0 or y < 0 or x >= n or y >= n or is_visited[x][y]:
            return
        is_visited[x][y] = True
        if arrays[x][y] <= k:
            return
        for mx, my in move:
            dx, dy = x + mx, y + my
            dfs(dx, dy)

    result = 0
    for k in range(max(map(max, arrays))):
        is_visited = [[False] * n for _ in range(n)]
        safe = 0
        for i in range(n):
            for j in range(n):
                if not is_visited[i][j] and arrays[i][j] > k:
                    dfs(i, j)
                    safe += 1
        result = max(result, safe)
    return result


n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
print(solution(n, arr))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(5, [
            [6, 8, 2, 6, 2],
            [3, 2, 3, 4, 6],
            [6, 7, 3, 3, 2],
            [7, 2, 5, 3, 6],
            [8, 9, 5, 2, 7]
        ])
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
