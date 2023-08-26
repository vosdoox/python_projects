# Tip calculator

# TODO 1: Greeting a user:
print("Welcome to the tip calculator.")

# TODO 2: Asking for a total amout of a bill:
bill = input("What was the total bill?")
bill_float = float(bill)

# TODO 3: Asking for the percentage of a tip:
tip = input("What percentage tip would you like to give? 10, 12 or 15?")
tip_int = int(tip)

# TODO 4: Asking for the number of people in a group:
people = input("How many people will split the bill?")
people_int = int(people)

# TODO 5: Calculating the tip:
result = bill_float/people_int*(1+tip_int/100)

# TODO 6: Rounding the result to two decimals:
result_rnd = round(result,2)
final_tot = "{:.2f}".format(result_rnd)
print(f"Each person should pay €{final_tot}")
