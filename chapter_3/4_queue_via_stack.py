# Answers to question 3.4. "Queue via Stack".
import unittest

from stack import Stack


# Time complexity:
# - enqueue: O(1)
# - dequeue: amortized O(|queue|)
class MyQueue:
    def __init__(self):
        self.reserve = Stack()
        self.ready = Stack()

    def enqueue(self, elem: int):
        self.reserve.push(elem)

    def dequeue(self) -> int:
        self._balance_stacks()
        return self.ready.pop()

    def _balance_stacks(self):
        if len(self.ready) == 0:
            while len(self.reserve) > 0:
                self.ready.push(self.reserve.pop())

    def __len__(self):
        return len(self.reserve) + len(self.ready)


class Test(unittest.TestCase):
    def test(self):
        queue = MyQueue()
        queue.enqueue(1)
        assert len(queue) == 1
        queue.enqueue(2)
        assert len(queue) == 2
        queue.enqueue(3)
        assert len(queue) == 3

        assert queue.dequeue() == 1
        assert len(queue) == 2
        assert queue.dequeue() == 2
        assert len(queue) == 1
        assert queue.dequeue() == 3
        assert len(queue) == 0

        queue.enqueue(1)
        assert len(queue) == 1
        queue.enqueue(2)
        assert len(queue) == 2

        assert queue.dequeue() == 1
        assert len(queue) == 1

        queue.enqueue(3)
        assert len(queue) == 2
        queue.enqueue(4)
        assert len(queue) == 3

        assert queue.dequeue() == 2
        assert len(queue) == 2
        assert queue.dequeue() == 3
        assert len(queue) == 1
        assert queue.dequeue() == 4
        assert len(queue) == 0


if __name__ == "__main__":
    unittest.main()
