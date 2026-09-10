class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)

    def age(self) -> None:
        self.age_days = self.age_days + 1

    def show(self) -> None:
        print(self.name + ":", str(self.height) + "cm,", self.age_days, "days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30)
    start_height = rose.height

    print("=== Garden Plant Growth ===")
    rose.show()
    for day in range(1, 8):
        print("=== Day", str(day), "===")
        rose.grow()
        rose.age()
        rose.show()

    growth = round(rose.height - start_height, 1)
    print("Growth this week:", str(growth) + "cm")
