from random import choice, randint

from data import data
from art import logo, vs
import random

SCORE = 0
is_game_continue = True
length_of_data = len(data)
print(length_of_data)
print(logo)

def pick():
    return data[randint(0, length_of_data-1)]

def get_info(choice):
    c_name = choice['name']
    c_desc = choice['description']
    c_country = choice['country']
    return f"{c_name}, Profession: {c_desc}, from {c_country}"

def find_winner(c1, c2):
    if c1['follower_count'] > c2['follower_count']:
        return 'a', c1
    else:
        c1 = c2
        return 'b', c1

choice1 = pick()
choice2 = pick()
if choice1 == choice2:
    choice2 = pick()

while is_game_continue:
    print(f"Compare A: {get_info(choice1)}")
    print(vs)
    print(f"Against B: {get_info(choice2)}")

    correct_answer, choice1 = find_winner(choice1, choice2)

    user = input("Who has more followers? Type 'A' or 'B':").lower()

    if user == correct_answer:
        SCORE += 1
        choice2 = pick()
        print(f"You're right! Current score: {SCORE}.")
    else:
        print(f"Sorry, that's wrong. Final score: {SCORE}")
        is_game_continue = False









