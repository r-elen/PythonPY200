import unittest

from task import DoubleLinkedNode
from task import DoubleLinkedList


class TestCaseDLL(unittest.TestCase):  # наследоваться от unittest.TestCase
    def test__getitem__(self):

        linkedlist = DoubleLinkedList([1, 2, 3])

        expected = 2
        actual = linkedlist.__getitem__(1)

        self.assertEqual(expected, actual)

    def test_repr_double_linked_node_without_prev_and_next(self):
        """
        Проверяет правильность вывода repr для узла без предыдущего и последующих узлов
        """

        node = DoubleLinkedNode(5)
        expected = "DoubleLinkedNode((5, None, None))"
        actual = repr(node)

        self.assertEqual(expected, actual)

    def test_repr_double_linked_node_without_prev(self):
        """
        Проверяет правильность вывода repr для узла без следующего узла
        """

        next_node = DoubleLinkedNode(3)
        current_node = DoubleLinkedNode(2)

        current_node.next = next_node
        next_node.prev = current_node

        expected = "DoubleLinkedNode((2, 'DoubleLinkedNode(3, None, None)', None))"
        actual = repr(current_node)
        # print(actual)

        self.assertEqual(expected, actual)

    def test_del_node(self):
        """
        Проверка удаления узла по индексу
        """

        double_ll = DoubleLinkedList([1, 2, 3])
        double_ll.del_node(1)

        expected = str([1, 3])
        actual = f"{double_ll}"

        self.assertEqual(expected, actual)

    def test_del_node_first(self):
        linkedlist = DoubleLinkedList([1, 2, 3])

        linkedlist.del_node(0)

        expected = str([2, 3])
        actual = f"{linkedlist}"

        self.assertEqual(expected, actual)

    def test_del_node_last(self):
        linkedlist = DoubleLinkedList([1, 2, 3])

        linkedlist.del_node(2)

        expected = str([1, 2])
        actual = f"{linkedlist}"

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    # Write your solution here
    pass