import unittest


def solution(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    left = [i for i in arr[1:] if i <= pivot]
    right = [i for i in arr[1:] if i > pivot]
    return solution(left) + [pivot] + solution(right)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([5, 3, 1, 4, 2])
        self.assertEqual(result, [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
