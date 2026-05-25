import sys


def parse(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for arg in args:
        part = arg.split(":")
        if len(part) != 2 or not part[0] or not part[1]:
            print(f"Error - invalid parameter '{arg}'")
            continue
        name: str = part[0]
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            inventory[name] = int(part[1])
        except ValueError as e:
            print(f"Quantity error for {name}: {e}")
    return inventory


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    args = sys.argv[1:]
    inventory = parse(args)
    if not inventory:
        print("Inventory is empty.")
        exit()
    print(f"Got inventory: {inventory}")
    items = list(dict.keys(inventory))
    print(f"Item list: {items}")
    quantity = sum(dict.values(inventory))
    print(f"Total quantity of the {len(items)} items: {quantity}")
    for item in items:
        qty = inventory[item]
        porcent: float = round((qty / quantity) * 100, 1)
        print(f"Item {item} represents {porcent}%")

    most: str = items[0]
    most_qty: int = inventory[items[0]]
    for item in items[1:]:
        if inventory[item] > most_qty:
            most_qty = inventory[item]
            most = item
    print(f"Item most abundant: {most} with quantity {most_qty}")
    least: str = items[0]
    least_qty: int = inventory[items[0]]
    for item in items[1:]:
        if inventory[item] < least_qty:
            least_qty = inventory[item]
            least = item
    print(f"Item most abundant: {least} with quantity {least_qty}")
    dict.update(inventory, {"magic_item": 1})
    print(f"Updated inventory: {inventory}")
