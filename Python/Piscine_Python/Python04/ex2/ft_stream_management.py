import sys
import typing


def print_error(message: str) -> None:
    sys.stderr.write("[STDERR] " + message + "\n")
    sys.stderr.flush()


def read_file(file_name: str) -> str:
    file: typing.IO[str] = open(file_name)
    content = file.read()
    file.close()
    return content


def transform_data(content: str) -> str:
    lines = content.splitlines()
    new_lines = []

    for line in lines:
        new_lines.append(line + "#")

    return "\n".join(new_lines) + "\n"


def save_file(file_name: str, content: str) -> bool:
    try:
        file: typing.IO[str] = open(file_name, "w")
        file.write(content)
        file.close()
        return True
    except Exception as error:
        print_error("Error opening file '" + file_name + "': " + str(error))
        return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
    else:
        file_name = sys.argv[1]
        print("=== Cyber Archives Recovery & Preservation ===")
        print("Accessing file '" + file_name + "'")
        try:
            content = read_file(file_name)
            print("---")
            print(content, end="")
            print("---")
            print("File '" + file_name + "' closed.")

            new_content = transform_data(content)
            print("Transform data:")
            print("---")
            print(new_content, end="")
            print("---")

            sys.stdout.write("Enter new file name (or empty): ")
            sys.stdout.flush()
            new_file_name = sys.stdin.readline().strip()
            if new_file_name == "":
                print("Not saving data.")
            else:
                print("Saving data to '" + new_file_name + "'")
                if save_file(new_file_name, new_content):
                    print("Data saved in file '" + new_file_name + "'.")
                else:
                    print("Data not saved.")
        except Exception as error:
            message = "Error opening file '" + file_name + "': " + str(error)
            print_error(message)
