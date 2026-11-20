# =========================================================
# NCV Level 4 - Day 4 AM PoE (Batch Processing)
# Tailored for the 5-digit learner numbers and specific errors
# =========================================================

def check_line(text):
    """Checks a line and returns an error message, or "" if valid."""
    parts = text.split(",")
    
    # 1. Check field count (must be exactly 3)
    if len(parts) != 3:
        return "expected 3 fields"
    
    student_number = parts[0].strip()
    name = parts[1].strip()
    marks_string = parts[2].strip()

    # 2. Check student number (Must be digits and exactly 5 digits for this file)
    if not (student_number.isdigit() and len(student_number) == 5):
        return "bad student number"
        
    # 3. Check name is not missing
    if name == "":
        return "missing name"
        
    # 4. Check marks
    for piece in marks_string.split(";"):
        piece = piece.strip()
        if piece == "": # Handles cases like 60;;80
            return "mark is not a number"
        if not piece.isdigit():
            # This catches "bad", "-5", etc.
            return "mark is not a number"
        if int(piece) > 100:
            return "mark above 100"
            
    return "" # All checks passed

# --- Main Batch Processing ---
good_lines = []
rejected_lines = []
error_counts = {}
seen_numbers = set() # To catch the duplicate at line 77

with open("learners.txt") as f:
    for line in f:
        text = line.strip()
        if not text:
            continue
            
        # Extract the student number for the duplicate check
        parts = text.split(",")
        num = parts[0].strip() if len(parts) > 0 else ""

        message = check_line(text)
        
        # Extra check for duplicates (Slide 18)
        if message == "" and num in seen_numbers:
            message = "duplicate student number"
        elif message == "":
            seen_numbers.add(num)
            
        if message == "":
            good_lines.append(text)
        else:
            rejected_lines.append(f"{text} <- {message}")
            error_counts[message] = error_counts.get(message, 0) + 1

# Step 2: Write clean.txt
with open("clean.txt", "w") as clean_file:
    for line in good_lines:
        clean_file.write(line + "\n")

# Write errors.log (Slide 17)
with open("errors.log", "w") as log:
    for entry in rejected_lines:
        log.write(entry + "\n")

# Step 1: Print the counts per reason
print("Rejected lines per reason:")
for reason, count in sorted(error_counts.items()):
    print(f" - {reason}: {count}")

# Step 3: Print percentage accepted
total_lines = len(good_lines) + len(rejected_lines)
if total_lines > 0:
    percent = (len(good_lines) / total_lines) * 100
    print(f"\nAcceptance rate: {percent:.1f}% ({len(good_lines)} out of {total_lines} lines)")