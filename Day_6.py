
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    for letter in original_text:

        if encode_or_decode == "decode":
            shift_amount *= -1

        shifted_index = alphabet.index(letter) + shift_amount
        shifted_index %= len(alphabet)
        output_text += alphabet[shifted_index]

    print(f"Your Result is here : {output_text}")


close = False
while not close:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    ask_to_continue = input("\tEnter 'yes' to continue / 'no' to close ?").lower()
    if ask_to_continue == "no":
        close = True
    else:
        close = False