import sys


if __name__ == "__main__":
    print("=== Command Quest ===")
    print("Program name:", sys.argv[0])

    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        print("Arguments received:", len(sys.argv) - 1)
        index = 1
        while index < len(sys.argv):
            print("Argument", str(index) + ":", sys.argv[index])
            index = index + 1

    print("Total arguments:", len(sys.argv))
