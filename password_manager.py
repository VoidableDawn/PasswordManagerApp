import random

LETTERS = ["a", "a", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
           "v",
           "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I",
           "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
SYMBOLS = ["!", "@", "#", "$", "%", "&", "*", "(", ")", ".", ",", ":", ";", "?", "/"]


def generate_password():
    # List Comprehension which adds between the ranges of 4 to 6 random letters from the letters
    # list to the pass_letters. Similarly for the numbers and symbols too
    pass_letters = [random.choice(LETTERS) for letter in range(random.randint(5, 7))]
    pass_symbols = [random.choice(SYMBOLS) for symbol in range(random.randint(2, 4))]
    pass_numbers = [random.choice(NUMBERS) for number in range(random.randint(3, 5))]
    pw = pass_letters + pass_symbols + pass_numbers
    random.shuffle(pw)
    password = "".join([char for char in pw])
    return password
