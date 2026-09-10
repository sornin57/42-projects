class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError("Invalid plant name to water: '" + plant_name + "'")
    print("Watering", plant_name + ": [OK]")


def test_watering_system(plants: list[str]) -> None:
    try:
        print("Opening watering system")
        for plant in plants:
            water_plant(plant)
    except PlantError as error:
        print("Caught PlantError:", error)
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")

    print("Testing valid plants...")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])

    print("Testing invalid plants...")
    test_watering_system(["Tomato", "lettuce", "Carrots"])

    print("Cleanup always happens, even with errors!")
