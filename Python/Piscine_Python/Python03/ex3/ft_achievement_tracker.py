import random


def gen_player_achievements() -> set[str]:
    all_achievements = [
        "First Steps",
        "Master Explorer",
        "Boss Slayer",
        "Treasure Hunter",
        "Crafting Genius",
        "World Savior",
        "Speed Runner",
        "Collector Supreme",
        "Hidden Path Finder",
        "Unstoppable",
        "Untouchable",
        "Strategist",
        "Survivor",
        "Sharp Mind",
    ]
    amount = random.randint(5, 9)
    achievements = random.sample(all_achievements, amount)
    return set(achievements)


def show_unique(player_name: str, player: set[str], others: set[str]) -> None:
    unique = player.difference(others)
    print("Only", player_name, "has:", unique)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print("Player Alice:", alice)
    print("Player Bob:", bob)
    print("Player Charlie:", charlie)
    print("Player Dylan:", dylan)

    all_achievements = alice.union(bob).union(charlie).union(dylan)
    common = alice.intersection(bob).intersection(charlie).intersection(dylan)

    print("All distinct achievements:", all_achievements)
    print("Common achievements:", common)

    show_unique("Alice", alice, bob.union(charlie).union(dylan))
    show_unique("Bob", bob, alice.union(charlie).union(dylan))
    show_unique("Charlie", charlie, alice.union(bob).union(dylan))
    show_unique("Dylan", dylan, alice.union(bob).union(charlie))

    print("Alice is missing:", all_achievements.difference(alice))
    print("Bob is missing:", all_achievements.difference(bob))
    print("Charlie is missing:", all_achievements.difference(charlie))
    print("Dylan is missing:", all_achievements.difference(dylan))
