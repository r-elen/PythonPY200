import unittest

from linkedlist import LinkedList


class TestCase(unittest.TestCase):  # наследоваться от unittest.TestCase
    def test__getitem__(self):

        linkedlist = LinkedList([1, 2, 3])

        expected = 2
        actual = linkedlist.__getitem__(1)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    # Write your solution here
    pass
