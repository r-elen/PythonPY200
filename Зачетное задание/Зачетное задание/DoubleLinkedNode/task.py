from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создание узла односвязного списка
        :param value: значение узла
        :param next_: ссылка на следующий узел (если нет, то None)
        """
        self.value = value
        self._next = next_  # self.next - вызывается next.setter

    @classmethod
    def is_valid(cls, node:Any) -> None:
        if not isinstance(node, (cls, type(None))):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name}({self.value}, {None})" if self.next is None \
            else f"{class_name}({self.value, class_name}({self.next})"  # TODO

    def __str__(self):
        return str(self.value)


class DoubleLinkedNode(Node):
    def __init__(self, value, next_: Optional["DoubleLinkedNode"] = None, prev_: Optional["DoubleLinkedNode"] = None):
        super().__init__(value, next_)
        self.prev = prev_

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev: Optional["DoubleLinkedNode"]):
        self.is_valid(prev)
        self._prev = prev

    def __repr__(self):
        next_repr = None if self.next is None \
            else f"{self.__class__.__name__}({self.next.value}, {None}, {None})"
        prev_repr = None if self.prev is None \
            else f"{self.__class__.__name__}({self.prev.value}, {None}, {None})"

        return f"{self.__class__.__name__}({self.value, next_repr, prev_repr})"


def test__node__str():  # пример кода для теста
    """

    :return:
    """
    node = Node(5)
    expected = ...  # шаблон
    actual = ...  #

    expected = 5
    actual = str(node)

    assert expected == actual


if __name__ == "__main__":
    doublinkednode = DoubleLinkedNode(1)
    print(repr(doublinkednode))
