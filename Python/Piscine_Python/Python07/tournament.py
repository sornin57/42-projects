from ex0 import AquaFactory, CreatureFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import AggressiveStrategy, BattleError, BattleStrategy
from ex2 import DefensiveStrategy, NormalStrategy


Opponent = tuple[CreatureFactory, BattleStrategy]


def make_creature(opponent: Opponent) -> object:
    return opponent[0].create_base()


def fight(first: Opponent, second: Opponent) -> None:
    first_creature = first[0].create_base()
    second_creature = second[0].create_base()

    print("* Battle *")
    print(first_creature.describe())
    print("vs.")
    print(second_creature.describe())
    print("now fight!")
    first[1].act(first_creature)
    second[1].act(second_creature)


def tournament(opponents: list[Opponent]) -> None:
    print("*** Tournament ***")
    print(len(opponents), "opponents involved")

    try:
        first_index = 0
        while first_index < len(opponents):
            second_index = first_index + 1
            while second_index < len(opponents):
                fight(opponents[first_index], opponents[second_index])
                second_index = second_index + 1
            first_index = first_index + 1
    except BattleError as error:
        print("Battle error, aborting tournament:", error)


if __name__ == "__main__":
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    tournament([
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ])

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    tournament([
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ])

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    tournament([
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ])
