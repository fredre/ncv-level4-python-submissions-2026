

def amount_due(facility_code, hours):

    rates = {"squa": 13.00, "swim": 12.00, "gym": 11.00, "wei": 8.00}
    
    if facility_code not in rates:
        return 0.0
        
    rate = rates[facility_code]
    return rate * hours

def final_amount(amount):
 
    VAT_RATE = 0.14
    return amount * (1 + VAT_RATE)

def display(name, final_amount):
 
    print("\n===================================")
    print("       MAXWELL'S FITNESS CENTRE    ")
    print("===================================")
    print(f"Customer Name : {name}")
    print(f"Total Due     : R{final_amount:.2f}")
    print("===================================")

def process_payment():
    
    print("--- New Transaction ---")
    
    name = input("Enter customer's name: ").strip()
    
    code = input("Enter facility code (squa/swim/gym/wei): ").strip().lower()
    
    # we were told no need to validate, but there it is:
    valid_codes = ["squa", "swim", "gym", "wei"]
    if code not in valid_codes:
        print("Error: Invalid facility code. Transaction cancelled.")
        return

    hours_text = input("Enter number of hours: ")
    
    try:
        hours = float(hours_text)
        if hours <= 0:
            print("Error: Hours must be a positive numeric value.")
            return
    except ValueError:
        print("Error: Hours must be a valid number.")
        return

    base_amount = amount_due(code, hours)
    
    total_payable = final_amount(base_amount)
    
    display(name, total_payable)


process_payment()


