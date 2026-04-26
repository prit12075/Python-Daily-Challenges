import copy

def create_inventory():
    return [
        {
            "item": "Laptop",
            "details": {"price": 50000, "stock": 10, "rating": 4.5}
        },
        {
            "item": "Phone",
            "details": {"price": 20000, "stock": 25, "rating": 4.2}
        },
        {
            "item": "Tablet",
            "details": {"price": 30000, "stock": 15, "rating": 4.0}
        }
    ]

def apply_discount(data, index):
    data[index]["details"]["price"] *= 0.9
    data[index]["details"]["stock"] += 5

def compare_data(original, modified):
    changed = 0
    unchanged = 0

    for i in range(len(original)):
        if original[i] == modified[i]:
            unchanged += 1
        else:
            changed += 1

    return (changed, unchanged)

inventory = create_inventory()

index = 8 % len(inventory)   # Personalization Rule

shallow = copy.copy(inventory)
deep = copy.deepcopy(inventory)

apply_discount(shallow, index)
apply_discount(deep, index)

print("Original Inventory:")
print(inventory)

print("\nShallow Copy:")
print(shallow)

print("\nDeep Copy:")
print(deep)

print("\nShallow Summary:", compare_data(inventory, shallow))
print("Deep Summary:", compare_data(inventory, deep))

print("\nExplanation:")
print("Shallow copy shares nested dictionaries with original data.")
print("Deep copy creates fully independent nested objects.")