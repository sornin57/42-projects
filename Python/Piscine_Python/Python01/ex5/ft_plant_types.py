class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age_days = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(self.name + ": Error, height can't be negative")
            return False
        self._height = height
        return True

    def set_age(self, age: int) -> bool:
        if age < 0:
            print(self.name + ": Error, age can't be negative")
            return False
        self._age_days = age
        return True

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days

    def grow(self) -> None:
        self._height = round(self._height + 2.1, 1)

    def age(self) -> None:
        self._age_days = self._age_days + 1

    def show(self) -> None:
        print(self.name + ":", str(self._height) + "cm,", self._age_days, "days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.has_bloomed = False

    def bloom(self) -> None:
        self.has_bloomed = True

    def show(self) -> None:
        super().show()
        print("Color:", self.color)
        if self.has_bloomed:
            print(self.name, "is blooming beautifully!")
        else:
            print(self.name, "has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print("Tree", self.name, "now produces a shade of", end=" ")
        print(str(self.get_height()) + "cm long and", str(self.trunk_diameter) + "cm wide.")

    def show(self) -> None:
        super().show()
        print("Trunk diameter:", str(self.trunk_diameter) + "cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self) -> None:
        super().grow()
        self.nutritional_value = self.nutritional_value + 1

    def age(self) -> None:
        super().age()

    def show(self) -> None:
        super().show()
        print("Harvest season:", self.harvest_season)
        print("Nutritional value:", self.nutritional_value)


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for day in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
