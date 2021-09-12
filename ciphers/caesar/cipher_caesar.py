alphabet_upper_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_upper_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_lower_en = 'abcdefghijklmnopqrstuvwxyz'
alphabet_lower_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
digits = '0123456789'


def encryption(letter, key, alphabet):
    position = alphabet.find(letter)
    new_position = (position + key) % len(alphabet)
    return alphabet[new_position]


def cipher_caesar_encrypt(message, key=3):
    encrypted_message = ''
    for letter in message:
        if letter in alphabet_upper_en:
            encrypted_message += encryption(letter, key, alphabet_upper_en)
        elif letter in alphabet_lower_en:
            encrypted_message += encryption(letter, key, alphabet_lower_en)
        elif letter in alphabet_upper_ru:
            encrypted_message += encryption(letter, key, alphabet_upper_ru)
        elif letter in alphabet_lower_ru:
            encrypted_message += encryption(letter, key, alphabet_lower_ru)
        elif letter in digits:
            encrypted_message += encryption(letter, key, digits)
        else:
            encrypted_message += letter
    return encrypted_message
