from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value

        # установить значение следующего узла с помощью метода set_next
        self.next_ = None
        self.set_next(next_)

    def __repr__(self) -> str:
        return f"Node({self.value}, {self.next_})"

    def is_valid(self, node: Any) -> None:
        # метод проверки корректности связываемого узла
        if not isinstance(node, (type(None), Node)):
            raise TypeError("Переданный в качестве аргумента узел не являектся объектом типа Node")

    def set_next(self, next_: Optional["Node"]) -> None:
        # метод должен проверять корректность узла и устанавливать значение атрибуту next
        if not isinstance(next_, (Node, type(None))):
            raise TypeError("Не корректный узел")
        self.next_ = next_


if __name__ == '__main__':
    # инициализируйте два узла с любыми значеними
    first_node = Node(1)
    second_node = Node(2)

    # свяжите первый узел со вторым
    first_node.set_next(second_node)

    print(first_node)
    print(second_node)
