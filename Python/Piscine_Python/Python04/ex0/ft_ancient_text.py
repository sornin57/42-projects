import sys
import typing


def read_file(file_name: str) -> str:
    file: typing.IO[str] = open(file_name)
    content = file.read()
    file.close()
    return content


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        file_name = sys.argv[1]
        print("=== Cyber Archives Recovery ===")
        print("Accessing file '" + file_name + "'")
        try:
            content = read_file(file_name)
            print("---")
            print(content, end="")
            print("---")
            print("File '" + file_name + "' closed.")
        except Exception as error:
            print("Error opening file '" + file_name + "':", error)
