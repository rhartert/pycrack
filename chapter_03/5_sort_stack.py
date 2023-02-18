# Answers to question 3.5 "Sort Stack".
import unittest

from stack import Stack


def sort_stack(stack: Stack) -> Stack:
    reordering = Stack()
    while len(stack) > 0:
        tmp = stack.pop()
        while len(reordering) > 0 and reordering.top() < tmp:
            stack.push(reordering.pop())
        reordering.push(tmp)

    return reordering


class Test(unittest.TestCase):
    test_cases = [
        [],
        [1],
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        [2, 4, 3, 1],
        [4, 2, 3, 2, 1, 4],
    ]

    def test(self):
        for seq in self.test_cases:
            # Create the stack to be sorted.
            stack = Stack()
            for i in seq:
                stack.push(i)

            ordered = sort_stack(stack)

            # Verify that the stack is sorted.
            order = []
            while len(ordered) > 0:
                order.append(ordered.pop())
            assert all(order[i] <= order[i + 1] for i in range(len(order) - 1))

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
