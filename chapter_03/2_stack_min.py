# Answers to question 3.2 "Stack Min".
import sys
import unittest

from stack import Stack


class MinStack:
    def __init__(self):
        self.stack = Stack()
        self.min_stack = Stack()

    def push(self, elem: int):
        self.stack.push(elem)
        if len(self.min_stack) == 0 or elem <= self.min_stack.top():
            self.min_stack.push(elem)

    def min(self) -> int:
        if len(self.min_stack) == 0:
            return sys.maxsize
        return self.min_stack.top()

    def top(self) -> int:
        if len(self.stack) == 0:
            return sys.maxsize
        return self.stack.top()

    def pop(self):
        if len(self.stack) == 0:
            return
        v = self.stack.pop()
        if self.min_stack.top() == v:
            self.min_stack.pop()


class Test(unittest.TestCase):
    def test(self):
        stack = MinStack()
        stack.push(3)
        assert stack.top() == 3
        assert stack.min() == 3
        stack.push(4)
        assert stack.top() == 4
        assert stack.min() == 3
        stack.push(2)
        assert stack.top() == 2
        assert stack.min() == 2
        stack.push(1)
        assert stack.top() == 1
        assert stack.min() == 1
        stack.pop()
        assert stack.top() == 2
        assert stack.min() == 2
        stack.pop()
        assert stack.top() == 4
        assert stack.min() == 3
        stack.pop()
        assert stack.top() == 3
        assert stack.min() == 3


if __name__ == "__main__":
    unittest.main()
