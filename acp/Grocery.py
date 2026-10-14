# ================================
# GROCERY COST COMPARISON TOOL
# ================================

print("=== GROCERY COST COMPARISON TOOL ===")

# ---------- PART 1: What did this week's shop cost per person? ----------
print("\nPART 1: What did this week's shop cost per person?")
rice_price = 12
milk_price = 4
fruit_price = 8
number_of_baskets = 2
family_members = 4
total_cost = (rice_price + milk_price + fruit_price) * number_of_baskets
cost_per_person = total_cost / family_members
print(f"The total cost of the shop is ${total_cost}.")
print(f"The cost per person is ${cost_per_person:.2f}.")

# ---------- PART 2: Can the items be shared equally? ----------
print("\nPART 2: Can the items be shared equally?")
rice_shares = number_of_baskets
milk_shares = number_of_baskets
fruit_shares = number_of_baskets
print(f"Rice can be shared among {rice_shares} people.")
print(f"Milk can be shared among {milk_shares} people.")
print(f"Fruit can be shared among {fruit_shares} people.")

# ---------- PART 3: Fix the weekly average ----------
print("\nPART 3: Fix the weekly average")
weekly_costs = [total_cost, 50, 60, 70]  # Example weekly costs
average_cost = sum(weekly_costs) / len(weekly_costs)
print(f"The average weekly cost over the last {len(weekly_costs)} weeks is ${average_cost:.2f}.")

# ---------- PART 4: Compare with three stores ----------
print("\nPART 4: Compare with three stores")
store_a_average = 70
store_b_average = 75
store_c_average = 80
print(f"Store A's average weekly cost is ${store_a_average:.2f}.")
print(f"Store B's average weekly cost is ${store_b_average:.2f}.")
print(f"Store C's average weekly cost is ${store_c_average:.2f}.")

# --------- PART 5: The summary ----------
print("\nPART 5: The summary")
print(f"Total cost of this week's shop: ${total_cost}")
print(f"Cost per person: ${cost_per_person:.2f}")
print(f"Average weekly cost over the last {len(weekly_costs)} weeks: ${average_cost:.2f}")