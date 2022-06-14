# Добавить методы add_water и remove_water

from typing import Union


class Glass:
    def __init__(self, capacity_volume: int, occupied_volume: int):  # создать класс Glass
        self.capacity_volume = None
        self.init_cap_vol(capacity_volume)

        self.occupied_volume = None
        self.init_occup_vol(occupied_volume)

    def init_cap_vol(self, capacity_volume: Union[int, float]):
        self.capacity_volume = capacity_volume

    def init_occup_vol(self, occupied_volume: Union[int, float]):
        self.occupied_volume = occupied_volume

    def add_water(self, add_volume: Union[int, float]):
        available_vol = self.capacity_volume - self.occupied_volume
        if add_volume > available_vol:
            raise ValueError("Слишком большое значение добавляемой воды")
        self.occupied_volume += add_volume

    def remove_water(self, remove_volume: Union[int, float]):
        if remove_volume > self.occupied_volume:
            raise ValueError("Слишком большое значение. В стакане меньше воды")
        self.occupied_volume += remove_volume


if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)

    glass.add_water(250)
    print(glass.capacity_volume, glass.occupied_volume)

    glass.remove_water(250)
    print(glass.capacity_volume, glass.occupied_volume)