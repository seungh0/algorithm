import unittest
import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline


def solution(n, m, components):
    is_visited = [False] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for x, y in components:
        graph[x].append(y)
        graph[y].append(x)

    def dfs(start):
        is_visited[start] = True
        for i in graph[start]:
            if not is_visited[i]:
                dfs(i)

    result = 0
    for i in range(1, n + 1):
        if not is_visited[i]:
            dfs(i)
            result += 1
    return result


n, m = map(int, input().split())
components = []
for i in range(m):
    components.append(list(map(int, input().split())))
print(solution(n, m, components))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution(6, 5, [[1, 2], [2, 5], [5, 1], [3, 4], [4, 6]])
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
