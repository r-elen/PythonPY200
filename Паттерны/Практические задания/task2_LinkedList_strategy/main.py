from typing import Iterable

from linked_list import LinkedList
from drivers import IStructureDriver
from factory_method import SimpleFileFactoryMethod


class LinkedListWithDriver(LinkedList):  # наследовать класс LinkedList
    def __init__(self, data: Iterable = None, driver: IStructureDriver = None):
        super().__init__(data)
        self.driver = driver  # расширяем конструктор, чтобы в связном списке был driver

    def read(self):
        """ С помощью драйвера считать данные и поместить их в LinkedList. """
        self.clear()  # считать данные из драйвера
        data = self.driver.read()
        for value in data:
            self.append(value)

    def write(self):
        """ С помощью драйвера записать данные из LinkedList. """
        self.driver.write(self)  # записать данные с помощью драйвера


if __name__ == '__main__':
    ll = LinkedListWithDriver()  # инициализировать пустой LinkedListWithDriver
    print("Считать данные из файла input.txt")
    driver_1 = SimpleFileFactoryMethod.get_driver()  # инициализировать драйвер и считать данные
    ll.driver = driver_1
    ll.read()
    print(ll)

    print("Записать данные в файл по умолчанию")
    driver_2 = SimpleFileFactoryMethod.get_driver()  # заменить драйвер и записать данные
    ll.driver = driver_2
    ll.write()
