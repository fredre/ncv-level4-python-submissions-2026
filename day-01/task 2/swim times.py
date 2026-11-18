# swimmers = list of (name, time_in_minutes) tuples
swimmers = []

name = input("Enter swimmer name (or x to finish): ")
while name != "x":
    text = input(f"Enter {name}'s time in minutes (e.g. 1.25 = 1 min 15s): ")

    # allow decimals, e.g. "1.5" or "12.75"
    try:
        time = float(text)
        if time <= 0:
            print("Invalid time — must be greater than 0.")
        else:
            swimmers.append((name, time))
    except ValueError:
        print("Invalid time.")

    name = input("Enter swimmer name (or x to finish): ")

if len(swimmers) == 0:
    print("No swimmers.")
else:
    total = 0
    for n, t in swimmers:
        total = total + t
    average = total / len(swimmers)

    # find fastest (lowest time) and slowest (highest time)
    fastest_name, fastest = swimmers[0]
    slowest_name, slowest = swimmers[0]

    for n, t in swimmers:
        if t < fastest:
            fastest = t
            fastest_name = n
        if t > slowest:
            slowest = t
            slowest_name = n

    print()
    print("===== SWIM TEAM REPORT =====")
    print(f"Swimmers : {len(swimmers)}")
    print(f"Average  : {average:.2f} min")
    print(f"Fastest  : {fastest_name} ({fastest:.2f} min)")
    print(f"Slowest  : {slowest_name} ({slowest:.2f} min)")
    print("-" * 35)

    # full roster, sorted fastest → slowest
    print(f"{'Name':<15}{'Time (min)':>12}")
    print("-" * 35)
    for n, t in sorted(swimmers, key=lambda s: s[1]):
        print(f"{n:<15}{t:>12.2f}")
    print("-" * 35)