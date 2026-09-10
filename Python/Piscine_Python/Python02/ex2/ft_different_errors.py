def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        result = 10 / 0
        print(result)
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        result = "Plant age: " + 10
        print(result)
    else:
        print("Operation completed successfully")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for number in [0, 1, 2, 3, 4]:
        print("Testing operation", str(number) + "...")
        try:
            garden_operations(number)
        except ValueError as error:
            print("Caught ValueError:", error)
        except ZeroDivisionError as error:
            print("Caught ZeroDivisionError:", error)
        except FileNotFoundError as error:
            print("Caught FileNotFoundError:", error)
        except TypeError as error:
            print("Caught TypeError:", error)

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
