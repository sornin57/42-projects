import math


def get_bad_value(parts: list[str]) -> str:
    for value in parts:
        try:
            float(value)
        except ValueError:
            return value.strip()
    return ""


def get_player_pos() -> tuple[float, float, float]:
    while True:
        text = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = text.split(",")

        try:
            x_text, y_text, z_text = parts
        except ValueError:
            print("Invalid syntax")
            continue

        try:
            x = float(x_text)
            y = float(y_text)
            z = float(z_text)
            return (x, y, z)
        except ValueError as error:
            print("Error on parameter '" + get_bad_value(parts) + "':", error)


def get_distance(
    first_pos: tuple[float, float, float],
    second_pos: tuple[float, float, float],
) -> float:
    x = second_pos[0] - first_pos[0]
    y = second_pos[1] - first_pos[1]
    z = second_pos[2] - first_pos[2]
    distance = math.sqrt((x ** 2) + (y ** 2) + (z ** 2))
    return round(distance, 4)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    first_pos = get_player_pos()
    print("Got a first tuple:", first_pos)
    print("It includes: X=" + str(first_pos[0]), end=", ")
    print("Y=" + str(first_pos[1]), end=", ")
    print("Z=" + str(first_pos[2]))

    center = (0.0, 0.0, 0.0)
    print("Distance to center:", get_distance(center, first_pos))

    print("Get a second set of coordinates")
    second_pos = get_player_pos()
    distance = get_distance(first_pos, second_pos)
    print("Distance between the 2 sets of coordinates:", distance)
