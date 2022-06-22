from typing import Iterable
from typing import Optional

from linked_list import LinkedList
from drivers import IStructureDriver
from factory_method import SimpleFileFactoryMethod, JsonFileDriverFactoryMethod


class LinkedListWithDriver(LinkedList):
    def __init__(self, data: Iterable = None, driver: IStructureDriver = None):
        super().__init__(data)
        self._driver = driver

    @property  # свойство для driver (getter + setter)
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self, driver: IStructureDriver):
        print("Вызван setter")
        self._driver = driver

    def read(self):
        """ С помощью драйвера считать данные и поместить их в LinkedList. """
        data_from_driver = self.driver.read()

        for value in data_from_driver:
            self.append(value)

    def write(self):
        """ С помощью драйвера записать данные из LinkedList. """
        self.driver.write(self)


if __name__ == '__main__':
    ll = LinkedListWithDriver()
    print("Считать данные из файла input.txt")
    ll.driver = SimpleFileFactoryMethod.get_driver()  # инициализировать SimpleFileDriver
    ll.read()
    print(ll)

    print("Записать данные в json файл по умолчанию")
    ll.driver = JsonFileDriverFactoryMethod.get_driver()  # инициализировать JsonFileDriver
    ll.write()
