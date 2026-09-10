import abc

from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability


class BattleError(Exception):
    pass


class BattleStrategy(abc.ABC):
    @abc.abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abc.abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, TransformCapability):
            message = (
                "Invalid Creature '"
                + creature.name
                + "' for this aggressive strategy"
            )
            raise BattleError(
                message
            )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, HealCapability):
            message = (
                "Invalid Creature '"
                + creature.name
                + "' for this defensive strategy"
            )
            raise BattleError(
                message
            )
        print(creature.attack())
        print(creature.heal())
