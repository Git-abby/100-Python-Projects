import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print('''************************************
Day 04 of 100 days of Python Project
************************************''')

print("Welcome to Password Generator")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#make a list for storing character
psw_chars = []

for i in range(0, nr_letters):
    psw_chars.append(random.choice(letters))

for i in range(0, nr_numbers):
    psw_chars.append(random.choice(numbers))

for i in range(0, nr_symbols):
    psw_chars.append(random.choice(symbols))

#shuffle the list, to make it stronger
random.shuffle(psw_chars)

#For storing into a string
final_password = ""
for chars in psw_chars:
    final_password += chars

print(final_password)


