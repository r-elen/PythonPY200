from typing import Any, Iterable, Optional

from node import Node, DoubleLinkedNode


class LinkedList:
    def __init__(self, data: Iterable = None):
        """
        Конструктор связаного списка

        :param data: передаваемы данные для добавления их в связанный список
        """
        self._len = 0
        self._head: Optional[Node] = None
        self._tail = self._head

        if data is not None:
            for value in data:
                self.append(value)

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Связывает два узла между собой

        :param left_node:
        :param right_node:
        """
        left_node._next = right_node

    def to_list(self):
        return [linked_value for linked_value in self]

    def __repr__(self):
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self):
        return f"{self.to_list()}"

    def index_is_valid(self, index):
        if not isinstance(index, int):
            raise TypeError()
        if not 0 <= index <= self._len - 1:
            raise IndexError("Значение индекса меньше 0 или больше длины списка")

    def step_by_step(self, index: int):
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self._len:  # для for
            raise IndexError()

        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    def __getitem__(self, index) -> Any:
        """
        Возвращает значение узла по указанному индексу
        :param index: индекс
        :return: значение узла по индексу
        """
        node = self.step_by_step(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """
        Устанавливает значение узла по указанному индексу
        :param index: индекс
        :param value:
        """
        node = self.step_by_step(index)
        node.value = value

    def __delitem__(self, index: int):
        """
        Удаление значения узла по индексу
        :param index: индекс удаляемого узла
        """
        node = self.step_by_step(index)
        node.value = None

    def __len__(self):
        """
        Подсчет длины связанного списка
        :return: кол-во узлов
        """
        len_ = 0
        for _ in self:  # TODO len
            len_ += 1
        return f"{len_}"

    def append(self, value: Any):
        """
        Добавление элемента в конец связного списка
        :param value: вставляемое значение
        """
        append_node = Node(value)

        if self._head is None:
            self._head = self._tail = append_node
        else:
            self.linked_nodes(self._tail, append_node)
            self._tail = append_node

        self._len += 1

    def insert(self, index, value):
        """
        Вставка узла по указанному индексу

        :param index: индекс
        :param value: значение
        :return: Связанный список с новым узлом
        """
        insert_node = Node(value)  # TODO insert

        if index == 0:
            next_node = self.step_by_step(index)

            self.linked_nodes(insert_node, next_node)  # вставка узла к начальному узлу
            self._head = insert_node
        elif index == self._len:
            self.append(value)
        else:
            prev_node = self.step_by_step(index-1)
            next_node = self.step_by_step(index)

            self.linked_nodes(prev_node, insert_node)  # вставка узла к предыдущему узлу
            self.linked_nodes(insert_node, next_node)  # вставка следующего узла к вставленному узлу

        self._len += 1

    def del_node(self, index):
        """
        Удаление узла по индексу
        :param index: индекс удаляемого узла
        """
        current_node = self.step_by_step(index)  # TODO delitem
        prev_node = self.step_by_step(index-1)
        next_node = self.step_by_step(index + 1)

        self.linked_nodes(prev_node, next_node)  # связываение предыдущего и следующего от текущего узла
        self._tail = next_node

        current_node.next = None

        self._len -= 1


class DoubleLinkedList(LinkedList):
    def __init__(self, data: Iterable = None):
        super().__init__(data)

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Cвязывает между собой два узла в обе стороны (от текущей к следующией и наоборот)

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node
        right_node.prev = left_node

    def insert(self, index, value):
        ...

    def append(self, value: Any):
        """
                Добавление элемента в конец связного списка
                :param value: вставляемое значение
                """
        append_node = DoubleLinkedNode(value)
        if self._head is None:
            self._head = self._tail = append_node
        else:
            self.linked_nodes(self._tail, append_node)
            self._tail = append_node

        self._len += 1

    def __delitem__(self, index):
        ...


if __name__ == "__main__":
    linked_list = LinkedList([1, 2, 3, 5])
    ll_with_insert = linked_list.insert(2, 8)
    print(ll_with_insert)

    # double_link_list = DoubleLinkedList([1, 2, 3])
    # print(double_link_list)
