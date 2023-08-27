# Pizza order service 

# TODO 1: Greet the customer:
print("Welcome to Python Pizza Deliveries!")

# TODO 2: Propose the available sizes of the pizza:
size = input("What size pizza do you want? S, M, or L ")

# TODO 3: Ask if a customer wants peperoni:
add_pepperoni = input("Do you want pepperoni? Y or N ")

# TODO 4: Ask if a customer wants extra cheese:
extra_cheese = input("Do you want extra cheese? Y or N ")

# TODO 5: Customize the pizza according to customer's choices and calculate the final price:
if size == "S":
  bill = 15
  if add_pepperoni == "Y":
    bill += 3
  elif extra_cheese == "Y":
    bill += 1
  print(f"Your final bill is ${bill}.")
elif size == "M":
  bill = 20
  if add_pepperoni == "Y":
    bill += 3
  elif extra_cheese == "Y":
    bill += 1
  print(f"Your final bill is ${bill}.")
elif size == "L":
  bill = 25
  if add_pepperoni == "Y":
    bill += 3
  elif extra_cheese == "Y":
    bill += 1

# TODO 6: Output the final bill:
  print(f"Your final bill is ${bill}.")
