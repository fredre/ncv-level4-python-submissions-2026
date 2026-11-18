import random

# ==========================================
# WishyWashy Carpet Cleaner - Reusable Modules
# ==========================================

# --- 1. Data Generation ---
def generate_minutes():
    """Returns a random integer between 30 and 180 (inclusive)."""
    return random.randint(30, 180)

# --- 2. Calculations ---
def calc_amount(machine_type, minutes):
    """Returns the amount before VAT, charging fractional hours proportionally."""
    rates = {
        "A": (50.00, 30.00),
        "B": (62.50, 36.25),
        "C": (74.87, 40.50)
    }
    
    machine_type = machine_type.upper()
    if machine_type not in rates:
        return 0.0
        
    hours = minutes / 60
    initial = rates[machine_type][0]
    hourly = rates[machine_type][1]
    
    return initial + (hourly * hours)

def calc_total_amount(amount):
    """Returns the VAT amount and total payable as a tuple."""
    vat = amount * 0.14
    total = amount + vat
    return vat, total

# --- 3. Reusable Statistics ---
def calc_stats(payments):
    """Calculates summary stats and returns them. Does NOT print."""
    if not payments:
        return 0, 0.0, 0.0, 0.0, 0.0
        
    total = 0
    highest = payments[0]
    lowest = payments[0]

    for p in payments:
        total += p
        if p > highest:
            highest = p
        if p < lowest:
            lowest = p

    average = total / len(payments)
    
    # Returns a tuple of 5 values
    return len(payments), total, average, highest, lowest

# --- 4. Output / Display ---
def print_invoice(name, machine_type, minutes, base_amount, vat, total):
    """Prints a single customer's invoice."""
    print("\n" + "-" * 35)
    print(f"INVOICE: {name}")
    print(f"Machine Type : {machine_type}")
    print(f"Usage Time   : {minutes} minutes")
    print(f"Amount (excl): R{base_amount:.2f}")
    print(f"VAT (14%)    : R{vat:.2f}")
    print(f"Total Payable: R{total:.2f}")
    print("-" * 35)

def display_summary(payments):
    """Receives the list, gets the stats, and displays the summary."""
    # Call the reusable stats function
    count, total, average, highest, lowest = calc_stats(payments)
    
    print("\n===================================")
    print("      WISHYWASHY DAILY SUMMARY     ")
    print("===================================")
    print(f"Customers Processed : {count}")
    print(f"Combined Total      : R{total:.2f}")
    print(f"Average Payment     : R{average:.2f}")
    print(f"Highest Payment     : R{highest:.2f}")
    print(f"Lowest Payment      : R{lowest:.2f}")
    print("===================================")

# --- 5. Main Driver ---
def process_payments():
    """Orchestrates the program by calling the reusable functions."""
    print("--- WishyWashy Carpet Cleaning ---")
    num_customers = int(input("Enter number of customers to process: "))
    
    payments = []
    
    for i in range(num_customers):
        print(f"\n--- Customer {i + 1} ---")
        name = input("Customer Name: ").strip()
        machine_type = input("Machine Type (A, B, or C): ").strip().upper()
        
        # Call the small, reusable functions
        minutes = generate_minutes()
        base_amount = calc_amount(machine_type, minutes)
        vat, total = calc_total_amount(base_amount)
        
        # Append to the list
        payments.append(total)
        
        # Call the display function for the invoice
        print_invoice(name, machine_type, minutes, base_amount, vat, total)

    # Call the display function for the summary
    display_summary(payments)

# Start the program
process_payments()