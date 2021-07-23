import unittest


def solution(s):
    stack = []
    for word in s:
        if stack and stack[-1] == word:
            stack.pop()
        else:
            stack.append(word)
    return 1 if len(stack) == 0 else 0


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = solution("baabaa")
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
