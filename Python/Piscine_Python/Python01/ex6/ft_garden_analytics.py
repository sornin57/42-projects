class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def add_grow(self) -> None:
            self._grow_calls = self._grow_calls + 1

        def add_age(self) -> None:
            self._age_calls = self._age_calls + 1

        def add_show(self) -> None:
            self._show_calls = self._show_calls + 1

        def show(self) -> None:
            print("Stats:", self._grow_calls, "grow,", end=" ")
            print(self._age_calls, "age,", self._show_calls, "show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age_days = age
        self.stats = Plant.Stats()

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def grow(self) -> None:
        self._height = round(self._height + 8.0, 1)
        self.stats.add_grow()

    def age(self) -> None:
        self._age_days = self._age_days + 1
        self.stats.add_age()

    def get_height(self) -> float:
        return self._height

    def show(self) -> None:
        self.stats.add_show()
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
    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def add_shade(self) -> None:
            self._shade_calls = self._shade_calls + 1

        def show(self) -> None:
            super().show()
            print(self._shade_calls, "shade")

    def __init__(self, name: str, height: float, age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.stats = Tree.TreeStats()

    def produce_shade(self) -> None:
        self.stats.add_shade()
        print("Tree", self.name, "now produces a shade of", end=" ")
        print(str(self.get_height()) + "cm long and", str(self.trunk_diameter) + "cm wide.")

    def show(self) -> None:
        super().show()
        print("Trunk diameter:", str(self.trunk_diameter) + "cm")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def age(self) -> None:
        self._age_days = self._age_days + 20
        self.stats.add_age()

    def grow(self) -> None:
        self._height = round(self._height + 30.0, 1)
        self.stats.add_grow()

    def show(self) -> None:
        super().show()
        print("Seeds:", self.seeds)


def show_statistics(plant: Plant) -> None:
    print("[statistics for", plant.name + "]")
    plant.stats.show()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print("Is 30 days more than a year? ->", Plant.is_older_than_year(30))
    print("Is 400 days more than a year? ->", Plant.is_older_than_year(400))

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    show_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    show_statistics(rose)

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    show_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    show_statistics(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    show_statistics(sunflower)

    print("=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    show_statistics(unknown)
