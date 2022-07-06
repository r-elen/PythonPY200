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

    def test_del_first_node_from_empty_list(self):
        linkedlist = LinkedList()

        with self.assertRaises(IndexError):
            linkedlist.del_node(0)

    def test_del_node_last(self):
        linkedlist = LinkedList([1, 2, 3])

        linkedlist.del_node(2)

        expected = str([1, 2])
        actual = f"{linkedlist}"

        self.assertEqual(expected, actual)
        self.assertEqual(str(linkedlist._tail), "2")

    def test_insert(self):
        linkedlist = LinkedList([1, 2, 3])

        linkedlist.insert(1, 8)

        expected = str([1, 8, 2, 3])
        actual = f"{linkedlist}"

        self.assertEqual(expected, actual)

    def test_insert_in_zero_point(self):
        linkedlist = LinkedList([1, 2, 3])

        linkedlist.insert(0, 8)

        expected = str([8, 1, 2, 3])
        actual = f"{linkedlist}"

        self.assertEqual(expected, actual)

    def test_len_insert_over_index(self):
        """когда индекс > len """
        # todo check len
        linkedlist = LinkedList([1, 2, 3])

        with self.assertRaises(IndexError):  # с помощью менеджера контакста и метода assertRaises проверить корректность вызываемой ошибки
            linkedlist.insert(index=25, value=8)

    def test_error_insert_after_last_node(self):
        """когда индекс равен len"""
        linkedlist = LinkedList([1, 2, 3])

        with self.assertRaises(
                IndexError):  # с помощью менеджера контакста и метода assertRaises проверить корректность вызываемой ошибки
            linkedlist.insert(index=3, value=8)

    def test_error_insert_over_index(self):
        """когда индекс > len """
        # todo check len
        linkedlist = LinkedList([1, 2, 3])

        with self.assertRaises(IndexError):  # с помощью менеджера контакста и метода assertRaises проверить корректность вызываемой ошибки
            linkedlist.insert(index=25, value=8)


if __name__ == "__main__":
    # Write your solution here
    pass