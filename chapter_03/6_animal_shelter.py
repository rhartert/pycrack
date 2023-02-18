# Answers to question 3.6. "Animal Shelter".
import unittest
from collections import deque


class AnimalShelter:
    def __init__(self):
        self.dogs = deque()
        self.cats = deque()
        self.order = 0

    def enqueueDog(self, dog: str):
        self.dogs.append((self.order, dog))
        self.order += 1

    def enqueueCat(self, cat: str):
        self.cats.append((self.order, cat))
        self.order += 1

    def dequeueDog(self) -> str:
        if len(self.dogs) == 0:
            return None
        _, dog = self.dogs.popleft()
        return dog

    def dequeueCat(self) -> str:
        if len(self.cats) == 0:
            return None
        _, cat = self.cats.popleft()
        return cat

    def dequeue(self) -> str:
        if len(self.cats) == 0:
            return self.dequeueDog()
        if len(self.dogs) == 0:
            return self.dequeueCat()

        order_dog, _ = self.dogs[0]
        order_cat, _ = self.cats[0]
        if order_dog < order_cat:
            return self.dequeueDog()
        else:
            return self.dequeueCat()


class Test(unittest.TestCase):
    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
