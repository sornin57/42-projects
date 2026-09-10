import elements
from . import elements as alchemy_elements


def healing_potion() -> str:
    return (
        "Healing potion brewed with '"
        + alchemy_elements.create_earth()
        + "' and '"
        + alchemy_elements.create_air()
        + "'"
    )


def strength_potion() -> str:
    return (
        "Strength potion brewed with '"
        + elements.create_fire()
        + "' and '"
        + elements.create_water()
        + "'"
    )
