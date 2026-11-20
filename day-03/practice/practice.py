# =========================================================
# NCV Level 4 - Day 3 PoE
# Collections, Aliasing, Nested Lists, and Records
# =========================================================

print("--- 1. ALIAS VS COPY (Slide 10) ---")
a = [1, 2, 3]
b = a         # Alias: both point to the same list
b.append(4)
print(f"Alias: a = {a}, b = {b}") 

c = [1, 2, 3]
d = c[:]      # Copy: creates a new list
d.append(4)
print(f"Copy:  c = {c}, d = {d}")


print("\n--- 2. THE FOUR COLLECTIONS (Slides 6-15) ---")
# List: ordered, changeable, duplicates allowed
marks_list = [65, 72, 48, 90, 55]
marks_list.append(81)

# Tuple: ordered, unchangeable
coordinates = (3, 4)

# Set: unordered, unique items only
codes = {"CS1", "CS2", "CS1", "CS3"}
codes.add("CS4")

# Dictionary: key-value pairs
learner = {"name": "Thandi", "mark": 65}
learner["city"] = "Soshanguve"
del learner["city"]

print(f"List: {marks_list}")
print(f"Tuple: {coordinates}")
print(f"Set (no duplicates): {codes}")
print(f"Dict: {learner}")


print("\n--- 3. NESTED LISTS (Slides 16-17) ---")
grid = [
    [65, 72, 58], 
    [48, 90, 55], 
    [81, 39, 77]
]
print(f"grid[1][2] is: {grid[1][2]}")

# Calculate the total for each row
print("Row totals:")
for row in grid:
    row_total = 0
    for value in row:
        row_total += value
    print(row_total)

# CHALLENGE from Slide 17: Find the highest value in the grid
highest = grid[0][0]
for row in grid:
    for value in row:
        if value > highest:
            highest = value
print(f"The highest value in the grid is: {highest}")


print("\n--- 4. DICTIONARY OF RECORDS (Slides 18-19) ---")
# The main goal from Slide 5
learners = {
    "2024001": {"name": "Thandi", "marks": [65, 72, 58]},
    "2024002": {"name": "Sipho", "marks": [48, 90, 55]}
}

# Read outside in: Dictionary -> Record -> List -> Index
print(f"Sipho's name: {learners['2024002']['name']}")
print(f"Thandi's second mark: {learners['2024001']['marks'][1]}")

# Add a new student to prove you can update records
learners["2024003"] = {"name": "Lerato", "marks": [88, 92, 85]}
print(f"Added Lerato. Total students: {len(learners)}")