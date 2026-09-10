import os
import site
import sys


def in_virtual_environment() -> bool:
    return sys.prefix != sys.base_prefix


def show_global_help() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print("Current Python:", sys.executable)
    print("Virtual Environment: None detected")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("To enter the construct, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate")
    print("matrix_env\\Scripts\\activate")
    print("Then run this program again.")


def show_virtual_environment() -> None:
    env_name = os.path.basename(sys.prefix)
    print("MATRIX STATUS: Welcome to the construct")
    print("Current Python:", sys.executable)
    print("Virtual Environment:", env_name)
    print("Environment Path:", sys.prefix)
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")
    print("Package installation path:")
    print(site.getsitepackages()[0])


if __name__ == "__main__":
    if in_virtual_environment():
        print("Inside the Construct")
        show_virtual_environment()
    else:
        print("Outside the Matrix")
        show_global_help()
