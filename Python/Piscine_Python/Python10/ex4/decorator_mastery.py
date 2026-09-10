import time
from collections.abc import Callable
from functools import wraps
from typing import Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print("Casting " + func.__name__ + "...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Spell completed in", str(round(end - start, 3)), "seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable[..., str]) -> Callable[..., str]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            power = args[-1]
            if isinstance(power, int) and power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable[..., str]) -> Callable[..., str]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            attempt = 1
            while attempt <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print("Spell failed, retrying...", end=" ")
                        print(
                            "(attempt "
                            + str(attempt)
                            + "/"
                            + str(max_attempts)
                            + ")"
                        )
                    attempt = attempt + 1
            return (
                "Spell casting failed after "
                + str(max_attempts)
                + " attempts"
            )

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        clean_name = name.replace(" ", "")
        return len(name) >= 3 and clean_name.isalpha()

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return (
            "Successfully cast "
            + spell_name
            + " with "
            + str(power)
            + " power"
        )


@spell_timer
def fireball() -> str:
    time.sleep(0.1)
    return "Fireball cast!"


@retry_spell(3)
def broken_spell() -> str:
    raise Exception("Spell failed")


@retry_spell(3)
def working_spell() -> str:
    return "Waaaaaaagh spelled !"


if __name__ == "__main__":
    print("Testing spell timer...")
    print("Result:", fireball())

    print("Testing retrying spell...")
    print(broken_spell())
    print(working_spell())

    print("Testing MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("Al1"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))
