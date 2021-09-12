from ciphers.rot13.change_message import ChangeMessage


class Decryption(ChangeMessage):
    """
    Класс для расшифровки сообщения
    """

    def change_letter(self, letter, alphabet):
        """
        Функция расшифрования символа
        :param letter: символ, который нужно расшифровать
        :param alphabet: алфавит, по которому расшифровывается символ
        :return: расшифрованный символ
        """
        position = alphabet.find(letter)
        new_position = (position - 13) % len(alphabet)
        return alphabet[new_position]
