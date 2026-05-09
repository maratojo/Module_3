import random

if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    player: list[str] = ["Alice", "bob", "Charlie",
                         "dylan", "Emma", "Gregory", "john", "kevin", "Liam"]
    print(f"Initial list of players: {player}")
    capitalize = []
    for name in player:
        capitalize.append(name.capitalize())
    print(f"New list with all names capitalized: {capitalize}")

    only_capitalize = []
    for name in player:
        if name == name.capitalize():
            only_capitalize.append(name)
    print(f"New list of capitalized names only: {only_capitalize}")
    score_dict = {}
    for name in player:
        score = random.randint(0, 999)
        score_dict.update({name: score})
    print(f"Score dict: {score_dict}")
    average: float = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {round(average, 2)}")
    high_score = {}
    for name, score in score_dict.items():
        if score > average:
            high_score.update({name: score})
    print(f"High scores: {high_score}")
