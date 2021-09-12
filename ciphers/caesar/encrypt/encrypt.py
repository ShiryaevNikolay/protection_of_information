def encrypt(letter, key, alphabet):
    """
    Функция шифрования символа
    :param letter: символ, который нужно зашифровать
    :param key: ключ, определяющий шаг для шифрования
    :param alphabet: алфавит, по которому шифруем
    :return: зашифрованный символ
    """
    position = alphabet.find(letter)
    new_position = (position + key) % len(alphabet)
    return alphabet[new_position]
