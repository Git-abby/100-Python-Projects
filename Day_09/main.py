import random
from art import logo

def deal_card():
    card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(card_list)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, s_score):
    if u_score == s_score:
        return "Draw 🙃"
    elif s_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif s_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > s_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    user_choice = []
    system_choice = []
    user_score = -1
    system_score = -1
    is_game_over = False

    for _ in range(2):
        user_choice.append(deal_card())
        system_choice.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_choice)
        system_score = calculate_score(system_choice)

        print(f"USER CARDS: {user_choice} Score: {user_score}")
        print(f"COMPUTER CARD: {system_choice[0]}")

        if user_score == 0 or system_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_choice.append(deal_card())
            else:
                is_game_over = True

    while system_score != 0 and system_score < 17:
        system_choice.append(deal_card())
        system_score = calculate_score(system_choice)

    print(f"Your Final Hand: {user_choice}, final Score: {user_score}")
    print(f"System's Final Hand: {system_choice}, final Score: {system_score}")
    print(compare(user_score, system_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)
    play_game()