# Starter Data (from the assignment)
learners = {
    "2024001": {"name": "Thandi", "marks": [65, 72, 58]},
    "2024002": {"name": "Sipho", "marks": [48, 90, 55]},
    "2024003": {"name": "Lerato", "marks": [81, 39, 77]},
    "2024004": {"name": "Dumisani", "marks": [72, 72, 48]},
    "2024005": {"name": "Naledi", "marks": [90, 55, 72]}
}

# =========================================================
# QUESTION 1: Collections and data structures (15 marks)
# =========================================================
print("--- QUESTION 1: Collections ---")

# 1.1 Create and print list of marks for 2024001
thandi_marks = learners["2024001"]["marks"]
print(f"Thandi's marks: {thandi_marks}")
print(f"First mark: {thandi_marks[0]}")
print(f"Last mark: {thandi_marks[-1]}")
print(f"Slice of first two: {thandi_marks[:2]}")

# 1.2 Tuple for fixed coordinate
# A tuple is appropriate here because the row and seat numbers should NOT 
# change once the classroom layout is set. Tuples are immutable.
coordinate = (3, 4)  # (row, seat)
row, seat = coordinate
print(f"Row: {row}, Seat: {seat}")

# 1.3 Set of module codes with a duplicate
module_codes = {"PROG1", "MATHS1", "PROG1", "ICT1"} 
print(f"Unique module codes: {len(module_codes)}")
print(f"Is 'PROG1' in codes? {'PROG1' in module_codes}")

# 1.4 Comments explaining structure choice
# A dictionary keyed by student number is used because student numbers 
# are unique and allow instant lookup (O(1)). A list of marks inside each 
# record is used because a learner will have multiple marks, and lists are 
# ordered and can grow over time.

# =========================================================
# QUESTION 2: First-principles list algorithms (20 marks)
# =========================================================
print("\n--- QUESTION 2: Algorithms ---")

def total_of(values):
    """Calculates total without using sum()."""
    total = 0
    for v in values:
        total = total + v
    return total

def mean_of(values):
    """Calculates mean. Handles empty list."""
    if len(values) == 0:
        return 0
    return total_of(values) / len(values)

def max_of(values):
    """Finds max without using max(). Handles empty list."""
    if len(values) == 0:
        return None
    highest = values[0]
    for v in values:
        if v > highest:
            highest = v
    return highest

def min_of(values):
    """Finds min without using min(). Handles empty list."""
    if len(values) == 0:
        return None
    lowest = values[0]
    for v in values:
        if v < lowest:
            lowest = v
    return lowest

def range_of(values):
    """Finds range using max_of and min_of."""
    if len(values) == 0:
        return 0
    return max_of(values) - min_of(values)

def above_mean(values):
    """Returns a list of values above the mean."""
    if len(values) == 0:
        return []
    avg = mean_of(values)
    result = []
    for v in values:
        if v > avg:
            result.append(v)
    return result

# Test data from the assignment
data = [65, 72, 48, 90, 55, 72, 48, 72]
print(f"Data: {data}")
print(f"Total: {total_of(data)}")
print(f"Mean: {mean_of(data)}")
print(f"Max: {max_of(data)}")
print(f"Min: {min_of(data)}")
print(f"Range: {range_of(data)}")
print(f"Above mean: {above_mean(data)}")

# =========================================================
# QUESTION 3: Search, duplicates and mode (15 marks)
# =========================================================
print("\n--- QUESTION 3: Search and Mode ---")

def find_first(values, target):
    """Returns first index or -1."""
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1

def find_all(values, target):
    """Returns all matching indices."""
    indices = []
    for i in range(len(values)):
        if values[i] == target:
            indices.append(i)
    return indices

def count_of(values, target):
    """Counts occurrences without using count()."""
    count = 0
    for v in values:
        if v == target:
            count = count + 1
    return count

def mode_of(values):
    """Returns a list of all modes using a frequency dictionary."""
    if len(values) == 0:
        return []
    
    freq = {}
    for v in values:
        if v in freq:
            freq[v] = freq[v] + 1
        else:
            freq[v] = 1
            
    highest_freq = max_of(list(freq.values()))
    
    modes = []
    for v in freq:
        if freq[v] == highest_freq:
            modes.append(v)
    return modes

print(f"First index of 72: {find_first(data, 72)}")
print(f"All indices of 72: {find_all(data, 72)}")
print(f"Count of 72: {count_of(data, 72)}")
print(f"Modes (tie demo): {mode_of([1, 2, 2, 3, 3])}")

# =========================================================
# QUESTION 4: Sorting algorithms (20 marks)
# =========================================================
print("\n--- QUESTION 4: Sorting ---")

def bubble_sort(values):
    """Bubble sort ascending. Returns a copy."""
    arr = values[:] # Make a copy!
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(values):
    """Selection sort ascending. Returns a copy."""
    arr = values[:] # Make a copy!
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Testing sorts
original = [65, 72, 48, 90, 55, 72, 48, 72]
print(f"Original: {original}")
print(f"Bubble Sorted: {bubble_sort(original)}")
print(f"Selection Sorted: {selection_sort(original)}")
print(f"Original after sorting (proves no change): {original}")

# Difference in swapping:
# Bubble sort swaps adjacent items repeatedly, pushing the largest to the end.
# Selection sort finds the absolute smallest item and swaps it once to the front.

# =========================================================
# QUESTION 5: Interactive learner records (20 marks)
# =========================================================
# (We put the menu in a function so it only runs when called, 
# but for the final program it runs at the bottom)

def display_ranking():
    """Displays descending ranking using tuples and bubble sort."""
    rank_list = []
    for number in learners:
        avg = mean_of(learners[number]["marks"])
        rank_list.append((avg, number))
        
    # Bubble sort descending based on the average (index 0 of tuple)
    n = len(rank_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if rank_list[j][0] < rank_list[j + 1][0]:
                rank_list[j], rank_list[j + 1] = rank_list[j + 1], rank_list[j]
                
    print("\n--- Ranking ---")
    for avg, number in rank_list:
        name = learners[number]["name"]
        print(f"{name} ({number}) - Average: {avg:.1f}")

def run_menu():
    """Main menu loop."""
    choice = ""
    while choice != "6":
        print("\n=== LEARNER SYSTEM ===")
        print("1. Add Learner")
        print("2. Search Learner")
        print("3. Update/Add Mark")
        print("4. Delete Learner")
        print("5. Show Ranking")
        print("6. Exit")
        choice = input("Choose (1-6): ")
        
        if choice == "1":
            num = input("New student number: ")
            if num in learners:
                print("Error: Duplicate number.")
            else:
                name = input("Name: ")
                marks_input = input("Marks (comma separated): ")
                marks_list = [int(m) for m in marks_input.split(",")]
                learners[num] = {"name": name, "marks": marks_list}
                print("Learner added.")
                
        elif choice == "2":
            num = input("Search student number: ")
            if num in learners:
                print(f"Found: {learners[num]['name']} - Marks: {learners[num]['marks']}")
            else:
                print("Learner not found.")
                
        elif choice == "3":
            num = input("Student number: ")
            if num in learners:
                print("1. Rename\n2. Add Mark")
                sub_choice = input("Pick: ")
                if sub_choice == "1":
                    learners[num]["name"] = input("New name: ")
                    print("Name updated.")
                elif sub_choice == "2":
                    mark = int(input("New mark: "))
                    learners[num]["marks"].append(mark)
                    print("Mark added.")
            else:
                print("Learner not found.")
                
        elif choice == "4":
            num = input("Student number to delete: ")
            if num in learners:
                del learners[num]
                print("Learner deleted.")
            else:
                print("Learner not found.")
                
        elif choice == "5":
            display_ranking()
            
        elif choice != "6":
            print("Invalid choice.")

# Start the interactive menu
run_menu()

# =========================================================
# QUESTION 6: Testing and submission (10 marks)
# =========================================================
# 6.1 Testing Evidence
# Test 1: Empty list
# Expected: mean_of([]) -> 0, max_of([]) -> None
# Actual: mean_of([]) -> 0, max_of([]) -> None
#
# Test 2: One mark
# Expected: mean_of([50]) -> 50.0, max_of([50]) -> 50
# Actual: mean_of([50]) -> 50.0, max_of([50]) -> 50
#
# Test 3: Repeated marks
# Expected: count_of([72,72,72], 72) -> 3
# Actual: count_of([72,72,72], 72) -> 3
#
# Test 4: Tied modes
# Expected: mode_of([1,2,2,3,3]) -> [2, 3]
# Actual: mode_of([1,2,2,3,3]) -> [2, 3]
#
# Test 5: Missing learner/target
# Expected: find_first([1,2,3], 9) -> -1, search for "999" -> "Learner not found."
# Actual: find_first([1,2,3], 9) -> -1, search for "999" -> "Learner not found."