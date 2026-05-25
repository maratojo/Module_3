import random


all_achievements = [
        "Crafting Genius", "Strategist", "World Savior", "Speed Runner",
        "Survivor", "Master Explorer", "Treasure Hunter", "Unstoppable",
        "First Steps", "Collector Supreme", "Untouchable", "Sharp Mind",
        "Boss Slayer", "Hidden Path Finder"
                    ]


def gen_player_achievements() -> set[str]:
    n = random.randint(5, 10)
    achievement = random.sample(all_achievements, n)
    return set(achievement)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements()
    }

    for name in players:
        print(f"Player {name}: {players[name]}")

    dist_achievement: set[str] = set()
    for name in players:
        dist_achievement = dist_achievement.union(players[name])
    print(f"\nAll distinct achievements: {dist_achievement}")

    common: set[str] = set()
    for name in players:
        if common == set():
            common = players[name]
        else:
            common = common.intersection(players[name])
    print(f"\nCommon achievements: {common}\n")

    for name in players:
        other_player: set[str] = set()
        for n in players:
            if n != name:
                other_player = other_player.union(players[n])
        unique = players[name].difference(other_player)
        print(f"only {name} has: {unique}")
    print()
    for name in players:
        alls = set(all_achievements)
        missing = alls.difference(players[name])
        print(f"{name} is missing: {missing}")
