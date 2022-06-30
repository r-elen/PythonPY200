import unittest

from task import Node


class TestCase(unittest.TestCase):  # наследоваться от unittest.TestCase
    def test_init_node_without_next(self):
        """Проверить следующий узел после инициализации с аргументом next_ по умолчанию"""
        node = Node(5)  # с помощью метода assertIsNone проверить следующий узел
        self.assertIsNone(node.next, msg="При иннициализации значение след узла НЕ None")

    def test_init_node_with_next(self):
        """Проверить следующий узел после инициализации с переданным аргументом next_"""
        second_node = Node("second")  # проверить что узлы связались
        first_node = Node("first", next_=second_node)

        expected = second_node
        actual = first_node.next
        self.assertIs(expected, actual, msg="Узлы не эквивалентны")

    def test_repr_node_without_next(self):
        """Проверить метод __repr__, для случая когда нет следующего узла."""
        node_value = 5
        node = Node(node_value)  # проверить метод __repr__ без следующего узла

        expected = f"Node({node_value}, None)"
        actual = repr(node)

        self.assertEqual(expected, actual, msg="Неверный repr для Node без след узла")

    @unittest.skip(reason="Тестим пропуск")  # пропустить тест с помощью декоратора unittest.skip
    def test_repr_node_with_next(self):
        """Проверить метод __repr__, для случая когда установлен следующий узел."""
        ...

    def test_str(self):
        some_value = 5
        node = Node(some_value)

        expected = str(some_value)

        self.assertEqual(str(node), expected)  # проверить строковое представление
        self.assertEqual(f"{node}", expected)

    def test_is_valid(self):
        example_node = Node(5)
        Node.is_valid(example_node)   # проверить метод is_valid при корректных узлах
        Node.is_valid(None)

        with self.assertRaises(TypeError):  # с помощью менеджера контакста и метода assertRaises проверить корректность вызываемой ошибки
            invalid_node = "Invalid_node"
            Node.is_valid(invalid_node)
