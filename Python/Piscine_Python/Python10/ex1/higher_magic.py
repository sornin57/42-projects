from collections.abc import Callable


Spell = Callable[[str, int], str]


def fireball(target: str, power: int) -> str:
    return "Fireball hits " + target + " with " + str(power) + " power"


def heal(target: str, power: int) -> str:
    return "Heal restores " + target + " for " + str(power) + " HP"


def spell_combiner(spell1: Spell, spell2: Spell) -> Spell:
    def combined_spell(target: str, power: int) -> str:
        first = spell1(target, power)
        second = spell2(target, power)
        return first + ", " + second

    return combined_spell


def power_amplifier(base_spell: Spell, multiplier: int) -> Spell:
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified_spell


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Spell,
) -> Spell:
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return conditional_spell


def spell_sequence(spells: list[Spell]) -> Callable[[str, int], list[str]]:
    def sequence(target: str, power: int) -> list[str]:
        results = []
        for spell in spells:
            results.append(spell(target, power))
        return results

    return sequence


if __name__ == "__main__":
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print("Combined spell result:", combined("Dragon", 10))

    print("Testing power amplifier...")
    amplified = power_amplifier(fireball, 3)
    print("Original:", fireball("Dragon", 10))
    print("Amplified:", amplified("Dragon", 10))

    print("Testing conditional caster...")
    strong_only = conditional_caster(
        lambda target, power: power >= 10,
        fireball,
    )
    print(strong_only("Dragon", 5))
    print(strong_only("Dragon", 20))

    print("Testing spell sequence...")
    sequence = spell_sequence([fireball, heal])
    print(sequence("Dragon", 10))

    print("Is fireball callable?", callable(fireball))
