# Answers to question 3.3 "Stack Of Plates".
import unittest

from stack import Stack


class SetOfStacks:
    def __init__(self, threshold: int):
        self.threshold = threshold
        self.stacks = []

    def push(self, elem: int):
        if len(self.stacks) == 0 or len(self.stacks[-1]) == self.threshold:
            self.stack_of_stacks.push(Stack())
            return
        self.stacks[-1].push(elem)

    def pop(self) -> int:
        self._clean_empty_stacks()
        return self.pop_at(len(self.stacks) - 1)

    def pop_at(self, index: int) -> int:
        if index < 0 or index >= len(self.stacks):
            return None
        if len(self.stacks[index]) == 0:
            return None
        return self.stacks[index].pop()

    def _clean_empty_stacks(self):
        while len(self.stacks) > 0 and len(self.stacks[-1]) == 0:
            self.stacks.pop(len(self.stacks - 1))


class Test(unittest.TestCase):
    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
