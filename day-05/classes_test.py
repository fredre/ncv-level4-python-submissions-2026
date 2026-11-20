class Chocolate:
    # 1. Constructor: sets initial values and protects the rule
    def __init__(self, name, price, weight):
        self.name = name
        # Guard rule: prevent negative price or weight
        self.price = price if price >= 0 else 0
        self.weight = weight if weight >= 0 else 0

    # 2. Setter (Mutator): changes the price safely
    def apply_discount(self, percent):
        if 0 <= percent <= 100:
            discount_amount = self.price * (percent / 100)
            self.price = round(self.price - discount_amount, 2)

    # 3. Getter (Accessor): reads and formats the chocolate's info
    def get_details(self):
        return f"{self.name} ({self.weight}g) - R{self.price:.2f}"


# --- Creating two objects ---
choc1 = Chocolate("Lunch Bar", 15.50, 62)
choc2 = Chocolate("Tex", 12.00, 40)

# --- Testing one method ---
print("Before discount:", choc1.get_details())
choc1.apply_discount(10)
print("After 10% discount:", choc1.get_details())  # Expected: Lunch Bar (62g) - R13.95
