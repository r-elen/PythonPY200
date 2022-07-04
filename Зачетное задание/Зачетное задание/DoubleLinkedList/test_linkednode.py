import unittest

from task import LinkedList


class TestCaseLL(unittest.TestCase):  # наследоваться от unittest.TestCase
    def test__getitem__(self):

        linkedlist = LinkedList([1, 2, 3])

        expected = 2
        actual = linkedlist.__getitem__(1)

        self.assertEqual(expected, actual)

    def test__setitem__(self):
        linkedlist = LinkedList([1, 2, 3])

        expected = str([1, 5, 3])

        linkedlist.__setitem__(1, 5)
        actual = f"{linkedlist}"

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    # Write your solution here
    pass