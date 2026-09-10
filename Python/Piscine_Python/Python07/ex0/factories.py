import abc

from .creatures import Aquabub, Creature, Flameling, Pyrodon, Torragon


class CreatureFactory(abc.ABC):
    @abc.abstractmethod
    def create_base(self) -> Creature:
        pass

    @abc.abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
