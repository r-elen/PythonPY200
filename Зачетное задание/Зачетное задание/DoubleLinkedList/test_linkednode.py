import unittest

from node import Node
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

    def test__delitem__(self):
        linkedlist = LinkedList([1, 2, 3])

        linkedlist.__delitem__(1)

        expected = str([1, None, 3])
        actual = f"{linkedlist}"

        self.assertEqual(expected, actual)

    def test_del_node(self):
        linkedlist = LinkedList([1, 2, 3])

        linkedlist.del_node(1)

        expected = str([1, 3])
        actual = f"{linkedlist}"

        self.assertEqual(expected, actual)

    def test_del_node_first(self):
        linkedlist = LinkedList([1, 2, 3])

        linkedlist.del_node(0)

        expected = str([2, 3])
        actual = f"{linkedlist}"

        self.assertEqual(expected, actual)

    def test_del_node_last(self):
        linkedlist = LinkedList([1, 2, 3])

        linkedlist.del_node(2)

        expected = str([1, 2])
        actual = f"{linkedlist}"

        self.assertEqual(expected, actual)

    def test_insert(self):
        linkedlist = LinkedList([1, 2, 3])

        linkedlist.insert(1, 8)

        expected = str([1, 8, 2, 3])
        actual = f"{linkedlist}"
        print(actual)

        self.assertEqual(expected, actual)

    def test_insert_in_zero_point(self):
        linkedlist = LinkedList([1, 2, 3])

        linkedlist.insert(0, 8)

        expected = str([8, 1, 2, 3])
        actual = f"{linkedlist}"

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    # Write your solution here
    pass