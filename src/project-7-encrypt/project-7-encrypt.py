import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(input_text, shift_number, cipher_direction):
    output_text = ""
    shift_number %= 26
    if cipher_direction == "decode":
        shift_number *= -1
    for i in input_text:
        if i in alphabet:
            if alphabet.index(i) + shift_number > 25:
                new_letter = alphabet[alphabet.index(i) + shift_number - 26]
            elif alphabet.index(i) + shift_number < 0:
                new_letter = alphabet[alphabet.index(i) + shift_number + 26]
            else:
                new_letter = alphabet[alphabet.index(i) + shift_number]
            output_text += new_letter
        else:
            output_text += i
    print(f"The {cipher_direction}d text is: {output_text}.")


x = True


def ui_improve():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(input_text=text, shift_number=shift, cipher_direction=direction)
        choice = input("Type 'yes' if you want to play again. Otherwise type 'no'.").lower()
        if choice != "yes":
            x = False
            print("Goodbye.")
    else:
        print("Invalid input, try again.")


print(art.logo)
ui_improve()
while ui_improve():
    ui_improve()

# # Another solution:
# x = True
# while x:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     if direction == "encode" or direction == "decode":
#         text = input("Type your message:\n").lower()
#         shift = int(input("Type the shift number:\n"))
#         caesar(input_text=text, shift_number=shift, cipher_direction=direction)
#         choice = input("Type 'yes' if you want to play again. Otherwise type 'no'.").lower()
#         if choice != "yes":
#             x = False
#             print("Goodbye.")
#     else:
#         print("Invalid input, try again.")
