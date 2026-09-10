import importlib
import sys
from typing import Any


def load_package(name: str) -> Any | None:
    try:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", "unknown")
        print("[OK]", name, "(" + version + ")")
        return module
    except ImportError:
        print("[MISSING]", name)
        return None


def show_install_help() -> None:
    print("Some programs are missing.")
    print("Install with pip:")
    print("pip install -r requirements.txt")
    print("Or install with Poetry:")
    print("poetry install")


def show_package_manager_info() -> None:
    print("pip uses requirements.txt")
    print("Poetry uses pyproject.toml")
    print("Current Python:", sys.executable)


def run_analysis(pandas: Any, numpy: Any, matplotlib: Any) -> None:
    pyplot = matplotlib.pyplot
    data = numpy.random.normal(50, 15, 1000)
    table = pandas.DataFrame({"signal": data})
    average = table["signal"].mean()

    print("Analyzing Matrix data...")
    print("Processing", len(table), "data points...")
    print("Average signal:", round(average, 2))
    print("Generating visualization...")

    table["signal"].plot(kind="hist", title="Matrix Signal")
    pyplot.savefig("matrix_analysis.png")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    pandas = load_package("pandas")
    numpy = load_package("numpy")
    matplotlib = load_package("matplotlib")

    show_package_manager_info()

    if pandas is None or numpy is None or matplotlib is None:
        show_install_help()
    else:
        run_analysis(pandas, numpy, matplotlib)
