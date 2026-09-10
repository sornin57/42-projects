import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if len(spells) == 0:
        return 0
    if operation == "add":
        return functools.reduce(operator.add, spells)
    if operation == "multiply":
        return functools.reduce(operator.mul, spells)
    if operation == "max":
        return functools.reduce(max, spells)
    if operation == "min":
        return functools.reduce(min, spells)
    raise ValueError("Unknown operation")


def base_enchantment(power: int, element: str, target: str) -> str:
    return (
        element
        + " enchantment on "
        + target
        + " with "
        + str(power)
        + " power"
    )


def partial_enchanter(
    base: Callable[[int, str, str], str],
) -> dict[str, Callable]:
    return {
        "fire": functools.partial(base, 50, "Fire"),
        "ice": functools.partial(base, 50, "Ice"),
        "storm": functools.partial(base, 50, "Storm"),
    }


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatch(value: Any) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(value: int) -> str:
        return "Damage spell: " + str(value) + " damage"

    @dispatch.register
    def _(value: str) -> str:
        return "Enchantment: " + value

    @dispatch.register
    def _(value: list) -> str:
        return "Multi-cast: " + str(len(value)) + " spells"

    return dispatch


if __name__ == "__main__":
    powers = [10, 20, 30, 40]
    print("Testing spell reducer...")
    print("Sum:", spell_reducer(powers, "add"))
    print("Product:", spell_reducer(powers, "multiply"))
    print("Max:", spell_reducer(powers, "max"))

    print("Testing partial enchanter...")
    enchantments = partial_enchanter(base_enchantment)
    print(enchantments["fire"]("Sword"))

    print("Testing memoized fibonacci...")
    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    print("Testing spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["fire", "ice", "heal"]))
    print(dispatcher({"unknown": True}))
