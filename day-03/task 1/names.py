# ============================================================
# File handling demo: write, read, modify, append, error-safe
# ============================================================

FILENAME = "names.txt"

# ------------------------------------------------------------
# 1. Write 5 names to names.txt, one per line
#    "w" mode creates the file (or overwrites it if it exists)
# ------------------------------------------------------------
names = ["Thabo", "Anke", "Sipho", "Lerato", "Naledi"]

with open(FILENAME, "w") as f:
    for name in names:
        f.write(name + "\n")       # \n = new line after each name

print("--- Step 1: wrote 5 names ---")


# ------------------------------------------------------------
# 2. Read back, strip each line, write in uppercase
#    "r" mode = read only. strip() removes the trailing \n.
# ------------------------------------------------------------
with open(FILENAME, "r") as f:
    lines = f.readlines()          # list of lines, each ending with \n

upper_names = []
for line in lines:
    clean = line.strip()           # remove \n (and any spaces)
    upper_names.append(clean.upper())

print("\n--- Step 2: names in uppercase ---")
for n in upper_names:
    print(n)


# ------------------------------------------------------------
# 3. Append a sixth name, then print the number of lines
#    "a" mode = append (adds to the end, does not overwrite)
# ------------------------------------------------------------
with open(FILENAME, "a") as f:
    f.write("Zanele\n")

# Count lines by reading the file again
with open(FILENAME, "r") as f:
    all_lines = f.readlines()

print(f"\n--- Step 3: appended 1 name. Total lines now: {len(all_lines)} ---")


# ------------------------------------------------------------
# 4. Read a file that does not exist — without crashing
#    try/except catches the FileNotFoundError
# ------------------------------------------------------------
print("\n--- Step 4: safe read of a missing file ---")

try:
    with open("does_not_exist.txt", "r") as f:
        content = f.read()
    print(content)
except FileNotFoundError:
    print("That file does not exist — but we handled it, no crash.")