class Date:
    def __init__(self, day: int, month: int, year: int):
        if not isinstance(day, int):
            raise TypeError
        self.day = day

        if not isinstance(day, int):
            raise TypeError
        self.month = month

        if not isinstance(day, int):
            raise TypeError
        self.year = year

    def __repr__(self):
        return f"{self.__class__.__name__}{self.day, self.month, self.year}"

    def __str__(self):
        day = self.day if self.day > 10 else f'0{self.day}'
        month = self.month if self.month > 10 else f'0{self.month}'
        return f"{day}/{month}/{self.year}"


if __name__ == '__main__':
    date = Date(1, 2, 1995)
    print(date)
