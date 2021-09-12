def encrypt(letter, key, alphabet):
    position = alphabet.find(letter)
    new_position = (position + key) % len(alphabet)
    return alphabet[new_position]
