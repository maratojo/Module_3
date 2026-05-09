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

    for name, ach in players.items():
        print(f"Player {name}: {ach}")

    dist_achievement: set[str] = set()
    for name, ach in players.items():
        dist_achievement = dist_achievement.union(ach)
    print(f"\nAll distinct achievements: {dist_achievement}")

    common: set[str] = set()
    for ach in players.values():
        if common == set():
            common = ach
        else:
            common = common.intersection(ach)
    print(f"\nCommon achievements: {common}\n")

    for name, ach in players.items():
        other_player: set[str] = set()
        for n, a in players.items():
            if n != name:
                other_player = other_player.union(a)
        unique = ach.difference(other_player)
        print(f"only {name} has: {unique}")
    print()
    for name, ach in players.items():
        all = set(all_achievements)
        missing = all.difference(ach)
        print(f"{name} is missing: {missing}")
