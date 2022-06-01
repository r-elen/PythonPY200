from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):

        if not isinstance(capacity_volume, (int, float)): # проверки на корректность данных
            raise TypeError("Не корректный тип данных")
        if capacity_volume <= 0:
            raise ValueError("Недопустимое значение")

        self.capacity_volume = capacity_volume  # инициализировать объект "Стакан"
        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    glass_1 = Glass(500, 100)  # инициализировать два объекта типа Glass
    glass_2 = Glass(200, 50)

    glass_3 = Glass(-100, 50)  # попробовать инициализировать НЕ корректные объекты
    glass_4 = Glass("100", 50)
