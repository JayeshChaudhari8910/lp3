def fractional_knapsack(weights, values, capacity):
    n = len(weights)
    ratios = [(values[i] / weights[i], weights[i], i) for i in range(n)]
    ratios.sort(reverse=True, key=lambda x: x[0])

    total_value = 0
    remaining_capacity = capacity
    items_selected = [0] * n  # Initialize a list to track which items are selected

    for ratio, weight, i in ratios:
        if remaining_capacity >= weight:
            total_value += ratio * weight
            remaining_capacity -= weight
            items_selected[i] = 1  # Mark the item as selected
        else:
            total_value += ratio * remaining_capacity
            items_selected[i] = remaining_capacity / weight
            break

    return total_value, items_selected

# Example usage
n = int(input("Enter the number of elements: "))
capacity = int(input("Enter the capacity of knapsack: "))
weights = []
values = []
for i in range(1, n + 1):
    z = int(input(f"Enter weight of {i}-th element: "))
    weights.append(z)
    z = int(input(f"Enter profit of {i}-th element: "))
    values.append(z)

max_value, items_selected = fractional_knapsack(weights, values, capacity)
print("Maximum value that can be obtained:", max_value)

# Print a Gantt chart table
print("Gantt Chart:")
print("Item  | Fraction Selected")
print("-" * 23)
for i in range(n):
    print(f"{i + 1} | {items_selected[i]:.2f}")
