import random


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")

    players = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]

    all_capitalized = [name.capitalize() for name in players]
    already_capitalized = [
        name for name in players if name == name.capitalize()
    ]
    scores = {name: random.randint(50, 1000) for name in all_capitalized}
    average = sum(scores.values()) / len(scores)
    high_scores = {
        name: score for name, score in scores.items() if score > average
    }

    print("Initial list of players:", players)
    print("New list with all names capitalized:", all_capitalized)
    print("New list of capitalized names only:", end=" ")
    print(already_capitalized)
    print("Score dict:", scores)
    print("Score average is", round(average, 2))
    print("High scores:", high_scores)
