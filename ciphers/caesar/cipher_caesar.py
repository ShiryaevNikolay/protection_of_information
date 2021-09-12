from alphabets import *
from encrypt.encrypt import encrypt


def cipher_caesar_encrypt(message, key=3):
    encrypted_message = ''
    for letter in message:
        if letter in alphabet_upper_en:
            encrypted_message += encrypt(letter, key, alphabet_upper_en)
        elif letter in alphabet_lower_en:
            encrypted_message += encrypt(letter, key, alphabet_lower_en)
        elif letter in alphabet_upper_ru:
            encrypted_message += encrypt(letter, key, alphabet_upper_ru)
        elif letter in alphabet_lower_ru:
            encrypted_message += encrypt(letter, key, alphabet_lower_ru)
        elif letter in digits:
            encrypted_message += encrypt(letter, key, digits)
        else:
            encrypted_message += letter
    return encrypted_message
