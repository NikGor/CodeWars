alphabet_dict = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
    't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
}

error_types = {
    TypeError: "Input must be a string"
}

def is_letter(char):
    return char.isalpha()

def get_alphabet_position(char):
    return alphabet_dict[char.lower()]

def alphabet_position(text):
    if not isinstance(text, str):
        raise error_types[TypeError]

    letters = filter(is_letter, text)
    positions = map(get_alphabet_position, letters)
    return ' '.join(map(str, positions))

print(alphabet_position("The sunset sets at twelve o' clock."))
