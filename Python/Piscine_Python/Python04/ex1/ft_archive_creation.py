import sys
import typing


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


def save_file(file_name: str, content: str) -> None:
    file: typing.IO[str] = open(file_name, "w")
    file.write(content)
    file.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
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

            new_file_name = input("Enter new file name (or empty): ")
            if new_file_name == "":
                print("Not saving data.")
            else:
                print("Saving data to '" + new_file_name + "'")
                save_file(new_file_name, new_content)
                print("Data saved in file '" + new_file_name + "'.")
        except Exception as error:
            print("Error opening file '" + file_name + "':", error)
