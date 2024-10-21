from art import logo

continue_bid = True
bid_dict = {}

print(logo)

while continue_bid:
    bidder = input("Enter name of bidder? ")
    bid = int(input("Enter the bid amount? $"))

    bid_dict[bidder] = bid

    another_bidder = input("is there any other bidder? 'yes' / 'no' ").lower()

    if another_bidder == 'no':
        continue_bid = False
    else:
        stop_bid = True
        print("\n"*20)

winner = max(bid_dict, key=bid_dict.get)
highest_bid = bid_dict[winner]

print(f"'{winner}' won the bid with bid of ${highest_bid}")
