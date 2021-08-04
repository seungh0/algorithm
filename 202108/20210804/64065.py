import unittest


def split_arr(param):
    result, arr = [], []
    temp = ""
    for i in param[1:-1]:
        if i == '}':
            if temp:
                arr.append(int(temp))
                temp = ""
            result.append(arr)
            arr = []
        elif i.isdigit():
            temp += i
        elif i == ',':
            if temp:
                arr.append(int(temp))
                temp = ""
    result.sort(key=len)
    return result


def calculate_tuple(result):
    arr = []
    for i in result:
        for j in i:
            if j not in arr:
                arr.append(j)
    return arr


def solution(param):
    arr = split_arr(param)
    return calculate_tuple(arr)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
        self.assertEqual(result, [2, 1, 3, 4])

    def test_something1(self):
        result = solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")
        self.assertEqual(result, [2, 1, 3, 4])

    def test_something2(self):
        result = solution("{{20,111},{111}}")
        self.assertEqual(result, [111, 20])

    def test_something3(self):
        result = solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
        self.assertEqual(result, [2, 1, 3, 4])


if __name__ == '__main__':
    unittest.main()
