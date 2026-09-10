def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True,
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: "* " + spell + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda mage: mage["power"], mages))
    return {
        "max_power": max(powers),
        "min_power": min(powers),
        "avg_power": round(sum(powers) / len(powers), 2),
    }


if __name__ == "__main__":
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Moon Ring", "power": 40, "type": "ring"},
    ]
    mages = [
        {"name": "Ada", "power": 80, "element": "fire"},
        {"name": "Bob", "power": 30, "element": "water"},
        {"name": "Chloe", "power": 90, "element": "air"},
    ]
    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(sorted_artifacts[0]["name"], "comes before", end=" ")
    print(sorted_artifacts[1]["name"])

    print("Testing power filter...")
    print(power_filter(mages, 50))

    print("Testing spell transformer...")
    print(" ".join(spell_transformer(spells)))

    print("Testing mage stats...")
    print(mage_stats(mages))
