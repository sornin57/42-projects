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

    def show(self) -> None:
        print(self.name + ":", str(self._height) + "cm,", self._age_days, "days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created:", end=" ")
    rose.show()

    if rose.set_height(25.0):
        print("Height updated: 25cm")
    else:
        print("Height update rejected")

    if rose.set_age(30):
        print("Age updated: 30 days")
    else:
        print("Age update rejected")

    if rose.set_height(-5.0):
        print("Height updated: -5cm")
    else:
        print("Height update rejected")

    if rose.set_age(-2):
        print("Age updated: -2 days")
    else:
        print("Age update rejected")

    print("Current state:", end=" ")
    rose.show()
