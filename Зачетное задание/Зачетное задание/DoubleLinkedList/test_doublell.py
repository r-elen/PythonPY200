import unittest

from task import DoubleLinkedList


class TestCaseDLL(unittest.TestCase):  # наследоваться от unittest.TestCase
    def test__getitem__(self):

        linkedlist = LinkedList([1, 2, 3])

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

        expected_value = "DoubleLinkedNode((2, 'DoubleLinkedNode(3, None, None)', None))"
        actual_value = repr(current_node)
        print(actual_value)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    # Write your solution here
    pass