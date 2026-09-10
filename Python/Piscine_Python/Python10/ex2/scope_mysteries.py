from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count = count + 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    total = initial_power

    def add_power(power: int) -> int:
        nonlocal total
        total = total + power
        return total

    return add_power


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchant(item_name: str) -> str:
        return enchantment_type + " " + item_name

    return enchant


def memory_vault() -> dict[str, Callable[..., Any]]:
    memory: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any:
        if key in memory:
            return memory[key]
        return "Memory not found"

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print("counter_a call 1:", counter_a())
    print("counter_a call 2:", counter_a())
    print("counter_b call 1:", counter_b())

    print("Testing spell accumulator...")
    accumulator = spell_accumulator(100)
    print("Base 100, add 20:", accumulator(20))
    print("Base 100, add 30:", accumulator(30))

    print("Testing enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("Testing memory vault...")
    vault = memory_vault()
    vault["store"]("secret", 42)
    print("Store 'secret' = 42")
    print("Recall 'secret':", vault["recall"]("secret"))
    print("Recall 'unknown':", vault["recall"]("unknown"))
