from hangman_art import stages, logo
from word_dictionary import word_list
import random

#Controll Game Over
isGameOver = False

#Lives / chances
lives = 6

#printing the logo
print(logo)

# Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(chosen_word)

# Create an empty String called placeholder.
placeholder = ""

# For each letter in the chosen_word, add a _ to placeholder.
for i in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

guessed_words = []

while not isGameOver:
    #Show user how many lives left
    print(f"********************({lives}/6) LEFT ********************")

    # Ask the user to guess a letter and assign their answer to a variable called guess. Make the String stored in guess lowercase.
    user_guess = input("Guess the letter? ").lower()

    #if user letter is already guessed
    if user_guess in guessed_words:
        print(f"You already guessed '{user_guess}'")

    # Create an empty string called "display".
    display = ""

    # Loop through each letter in the chosen_word
    for letter in chosen_word:
        if letter == user_guess:
            display += letter
            guessed_words.append(letter)
        elif letter in guessed_words:
            display += letter
        else:
            display += "_"

    print(f">>> {display}")

    # Game Over if all words are guessed
    if "_" not in display:
        isGameOver = True
        print("****************************YOU WIN****************************")

    #Controlling the flow of live on incorrect guess
    if user_guess not in chosen_word:
        lives -= 1
    #     Game over if lives = 0
        if lives == 0:
            isGameOver = True
            print(f"***********************YOU LOSE**********************")
            print(f"Correct word was '{chosen_word}'")

    print(stages[lives])

