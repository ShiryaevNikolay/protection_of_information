from ciphers.rot13.change_message import ChangeMessage


class Encryption(ChangeMessage):
    """
    Класс для шифрования сообщения
    """

    def change_letter(self, letter, alphabet):
        """
        Функция шифрования символа
        :param letter: символ, который нужно защифровать
        :param alphabet: алфавит, по которому шифруется символ
        :return: зашифрованный символ
        """
        position = alphabet.find(letter)
        new_position = (position + 13) % len(alphabet)
        return alphabet[new_position]
