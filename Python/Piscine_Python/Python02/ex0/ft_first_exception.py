def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)
    return temperature


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    try:
        print("Input data is '25'")
        temperature = input_temperature("25")
        print("Temperature is now", str(temperature) + "°C")
    except Exception as error:
        print("Caught input_temperature error:", error)

    try:
        print("Input data is 'abc'")
        temperature = input_temperature("abc")
        print("Temperature is now", str(temperature) + "°C")
    except Exception as error:
        print("Caught input_temperature error:", error)

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
