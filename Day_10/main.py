from art import logo, won, lose
import random

EASY_LEVEL = 10
HARD_LEVEL = 5

# RANDOM NUM BETWEEN 1 T 100
def game():
    num_to_guess = random.randint(1,100)
    # print(num_to_guess)
    is_game_over = False

    # SETTING UP THE DIFFICULTY LEVEL HERE;
    def set_difficulty():
        if input("Choose a difficulty. Type 'easy' or 'hard':").lower() == "hard":
            return HARD_LEVEL
        else:
            return EASY_LEVEL


    def find_guesses(u_guess, a, game_over):

        if u_guess == num_to_guess:
            print(won)
            print(f"You got it! The answer was {u_guess}.")
            game_over = True
            return a, game_over
        elif u_guess > num_to_guess:
            print("Too High.\nGuess again.")
        else:
            print("Too Low.\nGuess again.")
        return a - 1, game_over


    print(logo)
    print('''Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100''')
    attempts = set_difficulty() # Default 5 attempts

    while not is_game_over:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        attempts, is_game_over = find_guesses(user_guess, attempts, is_game_over)

        if attempts == 0:
            print(lose)
            print(f"You've run out of attempts. The number was {num_to_guess}!")
            is_game_over = True

while input("Do you want to play a Game to Guess A Number? yes / no ").lower() == "yes":
    game()
