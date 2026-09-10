def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)

    if temperature > 40:
        message = str(temperature) + "°C is too hot for plants (max 40°C)"
        raise Exception(message)
    if temperature < 0:
        message = str(temperature) + "°C is too cold for plants (min 0°C)"
        raise Exception(message)

    return temperature


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")

    tests = ["25", "abc", "100", "-50"]

    for value in tests:
        try:
            print("Input data is '" + value + "'")
            temperature = input_temperature(value)
            print("Temperature is now", str(temperature) + "°C")
        except Exception as error:
            print("Caught input_temperature error:", error)

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
