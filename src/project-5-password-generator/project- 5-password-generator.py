import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generateElement(base_elements, number_of_elements):
    ran_element = ''
    for i in range(0, number_of_elements):
        element = base_elements[random.randint(1, len(base_elements) - 1)]
        ran_element += element
    return ran_element


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Generate letters:
ran_letter = generateElement(letters, nr_letters)

# Generate symbols:
ran_symbol = generateElement(symbols, nr_symbols)

# Generate numbers:
ran_number = generateElement(numbers, nr_numbers)

combination = ran_letter + ran_symbol + ran_number
ranPassword = random.sample(combination, len(combination))
password = "".join(map(str, ranPassword))
print("The generated password is: " + password)
