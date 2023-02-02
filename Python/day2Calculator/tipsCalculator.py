print("\nWelcome to the tip calculator.\n")
total_bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

p_tip = tip / 100
pay = round(total_bill * (p_tip+1) / people, 2)


print(f"Each person should pay ${pay}")
