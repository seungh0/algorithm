import unittest
import re


def solution(new_id):
    # 1
    new_id = new_id.lower()

    # 2
    new_id = re.sub(r"[^a-z0-9-_.]", "", new_id)

    # 3
    while '..' in new_id:
        new_id = new_id.replace("..", '.')

    # 4
    while True:
        if new_id.startswith("."):
            new_id = new_id[1:]
        else:
            break
    while True:
        if new_id.endswith("."):
            new_id = new_id[:-1]
        else:
            break

    # 5
    if not new_id:
        new_id = "a"

    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            return new_id[:-1]

    # 7
    if len(new_id) <= 2:
        return new_id + new_id[-1] * (3 - len(new_id))
    return new_id


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution("...!@BaT#*..y.abcdefghijklms")
        self.assertEqual(result, "bat.y.abcdefghi")

    def test_something1(self):
        result = solution("123_.def")
        self.assertEqual(result, "123_.def")

    def test_something3(self):
        result = solution("=.=")
        self.assertEqual(result, "aaa")

    def test_something4(self):
        result = solution("......a......a......a....")
        self.assertEqual(result, "a.a.a")

    def test_something2(self):
        result = solution("abcdefghijklmn.p")
        self.assertEqual(result, "abcdefghijklmn")


if __name__ == '__main__':
    unittest.main()
