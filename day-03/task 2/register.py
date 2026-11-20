# =========================================================
# NCV Level 4 - Day 3 PM PoE
# Learner Register: Dictionaries, Lists, and Algorithms
# =========================================================

def add_learner(learners, number, name):
    """Adds a learner if the 7-digit number doesn't exist."""
    if len(number) != 7:
        return False
    if number in learners:
        return False
    learners[number] = {"name": name, "marks": []}
    return True

def add_mark(learners, number, mark):
    """Adds a mark (0-100) to a learner."""
    if number not in learners:
        return False
    if mark < 0 or mark > 100:
        return False
    learners[number]["marks"].append(mark)
    return True

def rename_learner(learners, number, new_name):
    """Renames an existing learner."""
    if number not in learners:
        return False
    learners[number]["name"] = new_name
    return True

def delete_learner(learners, number):
    """Deletes a learner from the register."""
    if number not in learners:
        return False
    del learners[number]
    return True

def find_by_name(learners, search_text):
    """Returns a list of (number, name) tuples matching the search."""
    results = []
    search_text = search_text.lower()
    for number, record in learners.items():
        if search_text in record["name"].lower():
            results.append((number, record["name"]))
    return results

def learner_average(learners, number):
    """Calculates the average mark for a learner. Returns None if no marks."""
    if number not in learners or len(learners[number]["marks"]) == 0:
        return None
    total = sum(learners[number]["marks"])
    return total / len(learners[number]["marks"])

def ranking(learners):
    """Returns a sorted list of (average, number) tuples, highest first."""
    rank_list = []
    for number in learners:
        avg = learner_average(learners, number)
        if avg is not None:
            rank_list.append((avg, number))
    
    # Bubble sort descending
    n = len(rank_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if rank_list[j][0] < rank_list[j + 1][0]:
                rank_list[j], rank_list[j + 1] = rank_list[j + 1], rank_list[j]
    return rank_list

def print_ranking(learners):
    """Prints the ranking table."""
    print("\n--- Class Ranking ---")
    ranks = ranking(learners)
    if not ranks:
        print("No marks recorded yet.")
        return
    for position, (avg, number) in enumerate(ranks, 1):
        name = learners[number]["name"]
        print(f"{position}. {name} ({number}) - Average: {avg:.1f}%")

def main():
    learners = {}
    choice = ""
    
    while choice != "7":
        print("\n=== LEARNER REGISTER ===")
        print("1. Add Learner")
        print("2. Add Mark")
        print("3. Rename Learner")
        print("4. Delete Learner")
        print("5. Find by Name")
        print("6. Show Ranking")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ")
        
        if choice == "1":
            num = input("Enter 7-digit student number: ")
            name = input("Enter learner name: ")
            if add_learner(learners, num, name):
                print(f"Success: {name} added.")
            else:
                print("Error: Invalid number or duplicate student number.")
                
        elif choice == "2":
            num = input("Enter student number: ")
            try:
                mark = int(input("Enter mark (0-100): "))
                if add_mark(learners, num, mark):
                    print("Mark added.")
                else:
                    print("Error: Invalid student number or mark.")
            except ValueError:
                print("Error: Mark must be a number.")
                
        elif choice == "3":
            num = input("Enter student number: ")
            new_name = input("Enter new name: ")
            if rename_learner(learners, num, new_name):
                print("Name updated.")
            else:
                print("Error: Student number not found.")
                
        elif choice == "4":
            num = input("Enter student number to delete: ")
            if delete_learner(learners, num):
                print("Learner deleted.")
            else:
                print("Error: Student number not found.")
                
        elif choice == "5":
            text = input("Enter name to search: ")
            results = find_by_name(learners, text)
            if results:
                print(f"Found {len(results)} result(s):")
                for num, name in results:
                    print(f" - {num}: {name}")
            else:
                print("No learners found with that name.")
                
        elif choice == "6":
            print_ranking(learners)
            
        elif choice == "7":
            print("Goodbye.")
        else:
            print("Invalid choice. Please pick 1-7.")

if __name__ == "__main__":
    main()