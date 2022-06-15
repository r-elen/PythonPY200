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
        self.next = next_  # вызовется setter

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def is_valid(cls, node: Any) -> None:
        if not isinstance(node, (cls, type(None))):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_


class DoubleLinkedNode(Node):
    def __init__(self, value, next_: Optional["DoubleLinkedNode"] = None, prev: Optional["DoubleLinkedNode"] = None):
        super().__init__(value, next_)
        self.prev = prev

    def __repr__(self):
        next_repr: str = None if self.next is None \
            else f"{self.__class__.__name__}({self.next.value}, {None}, {None})"
        prev_repr: str = None if self.prev is None \
            else f"{self.__class__.__name__}({self.prev.value}, {None}, {None})"

        return f"{self.__class__.__name__}({self.value, next_repr, prev_repr})"

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev: Optional["Node"]):
        self.is_valid(prev)
        self._prev = prev


if __name__ == '__main__':
    doublenode = DoubleLinkedNode(1)
    print(repr(doublenode))
