import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = user.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        format: list[float] = []
        try:
            for part in parts:
                format.append(float(part.strip()))
            return (format[0], format[1], format[2])
        except ValueError as e:
            print(f"Error on parameter '{part.strip()}': {e}")

def distance(pos1: tuple[float, float, float],
             pos2: tuple[float, float, float]) -> float:
    pos = math.sqrt(((pos2[0] - pos1[0]) ** 2) + ((pos2[1] - pos1[1]) ** 2) +
                    ((pos2[2] - pos1[2]) ** 2))
    return pos


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("\nGet a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    distance_1 = round(distance(pos1, (0.0, 0.0, 0.0)), 4)
    print(f"Distance to center: {distance_1}")
    print("\nGet a second set of coordinates")
    pos2 = get_player_pos()
    distance_2 = round((distance(pos1, pos2)), 4)
    print(f"Distance between the 2 sets of coordinates: {distance_2}")
