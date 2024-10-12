print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
black_Olives = input("Do you want Black Olives on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0


#To Do : Work on Pizza's Size
if size == "S":
    print("Small Size Pizza $15")
    bill += 15
elif size == "M":
    print("Medium Size Pizza $20")
    bill += 20
elif size == "L":
    print("Large Size Pizza $25")
    bill += 25
else:
    print(f"I don't understand your input[size]? {size}.")

#To Do : Work on Topping - Black Olive's
if black_Olives == "Y":
    if size == "S":
        print("+Black Olives $2")
        bill += 2
    else:
        print("+Black Olives $3")
        bill += 3
else:
    if black_Olives == "N":
        bill += 0
    else:
        print(f"I don't understand your input[Black Olives]? {black_Olives}.")


#To Do : Work on Extra Cheese
if extra_cheese == "Y":
    print("+Cheese $1")
    bill += 1
else:
    if extra_cheese == "N":
        bill += 0
    else:
        print(f"I don't understand your input[Extra Cheese]? {extra_cheese}.")


print(f"Your final bill is: ${bill}.")








