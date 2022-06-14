class Glass:
    def __init__(self, capacity_volume, occupied_volume):
        self.capacity_volume = capacity_volume  # объем стакана
        self.occupied_volume = occupied_volume  # объем жидкости в стакане


if __name__ == "__main__":
    glass = Glass(100, 50)

    print(type(glass))
    print(glass.__class__)

    print(type(glass) == glass.__class__)
