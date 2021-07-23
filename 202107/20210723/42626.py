import unittest
import heapq


def solution(nums, k):
    arr = []
    for num in nums:
        heapq.heappush(arr, num)

    cnt = 0
    while True:
        one = heapq.heappop(arr)
        if one >= k:
            return cnt

        if not arr:
            return -1

        two = heapq.heappop(arr)
        heapq.heappush(arr, one + two * 2)
        cnt += 1


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution([1, 2, 3, 9, 10, 12], 7)
        self.assertEqual(result, 2)

    def test_something1(self):
        result = solution([0, 0, 0, 0], 2)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
