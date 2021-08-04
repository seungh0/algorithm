import unittest


def solution(arr, target):
    left = 0
    right = len(arr) - 1

    mid = (left + right) // 2

    while left <= right:
        if arr[mid] < target:  # 5 < 7
            left = mid + 1
        elif arr[mid] > target:  # 3 < 5
            right = mid - 1
        else:  # arr[mid] == target
            return mid
    return -1  # Not Found


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([1, 3, 5, 7, 9], 3)
        self.assertEqual(result, 1)

    def test_something1(self):
        result = solution([1, 3, 5, 7, 9], 8)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
