import sys


def get_inventory() -> dict[str, int]:
    inventory = {}
    index = 1

    while index < len(sys.argv):
        parameter = sys.argv[index]
        parts = parameter.split(":")

        if len(parts) != 2:
            print("Error - invalid parameter '" + parameter + "'")
        elif parts[0] in inventory:
            print("Redundant item '" + parts[0] + "' - discarding")
        else:
            try:
                inventory[parts[0]] = int(parts[1])
            except ValueError as error:
                print("Quantity error for '" + parts[0] + "':", error)
        index = index + 1

    return inventory


def get_most_item(inventory: dict[str, int]) -> str:
    items = list(inventory.keys())
    most_item = items[0]

    for item in items:
        if inventory[item] > inventory[most_item]:
            most_item = item

    return most_item


def get_least_item(inventory: dict[str, int]) -> str:
    items = list(inventory.keys())
    least_item = items[0]

    for item in items:
        if inventory[item] < inventory[least_item]:
            least_item = item

    return least_item


def show_inventory(inventory: dict[str, int]) -> None:
    items = list(inventory.keys())
    total = sum(inventory.values())

    print("Got inventory:", inventory)
    print("Item list:", items)
    print("Total quantity of the", len(items), "items:", total)

    for item in items:
        percent = inventory[item] * 100 / total
        print("Item", item, "represents", str(round(percent, 1)) + "%")

    most_item = get_most_item(inventory)
    least_item = get_least_item(inventory)

    print("Item most abundant:", most_item, end=" ")
    print("with quantity", inventory[most_item])
    print("Item least abundant:", least_item, end=" ")
    print("with quantity", inventory[least_item])


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    inventory = get_inventory()
    if len(inventory) == 0:
        print("Inventory is empty")
    else:
        show_inventory(inventory)
        inventory.update({"magic_item": 1})
        print("Updated inventory:", inventory)
