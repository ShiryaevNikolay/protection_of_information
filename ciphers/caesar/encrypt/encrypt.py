def encrypt(letter, key, alphabet):
    """
    Фцнкия шифрования сообщения
    """
    position = alphabet.find(letter)
    new_position = (position + key) % len(alphabet)
    return alphabet[new_position]
