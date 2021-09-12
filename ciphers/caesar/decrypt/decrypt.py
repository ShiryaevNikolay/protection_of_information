def decrypt(letter, key, alphabet):
    """
    Функция для дешифрования символа
    :param letter: символ, который нужно дешифровать
    :param key: ключ, определяющий шаг для дешифрования
    :param alphabet: алфавит, по которому дешифруем
    :return: дешифрованный символ
    """
    position = alphabet.find(letter)
    new_position = (position - key) % len(alphabet)
    return alphabet[new_position]
