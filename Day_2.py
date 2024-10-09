print('''************************************
Day 02 of 100 days of Python Project
************************************''')

print("Welcome to the tip calculator!")
# User Inputs
bill = float(input("What was the total bill? $"))
tip = int(input("What the percentage of tip you like to give? 10, 12, 15 "))
people = int(input("How many people to split the bill into? "))

# Calculating % of tip from bill
# Ex: 100 bill > 10% > should be 10$ tip
percentage_of_tip = tip / 100 * bill

#Total bill = bill + tip = 100 + 10 = 110
#round(number, number pf digits)
total_bill = round((bill + percentage_of_tip) / people, 2)

print(f"Each person should pay: ${total_bill}")
