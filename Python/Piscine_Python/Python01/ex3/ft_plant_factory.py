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
        print("Created:", self.name + ":", str(self.height) + "cm,", self.age_days, "days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)

    print("=== Plant Factory Output ===")
    rose.show()
    oak.show()
    cactus.show()
    sunflower.show()
    fern.show()
