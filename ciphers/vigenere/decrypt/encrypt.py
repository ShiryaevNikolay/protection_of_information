from ciphers.vigenere.change_message import ChangeMessage


class Encryption(ChangeMessage):

    def change_letter(self, letter, index, alphabet):
        """
        Функиця, которая шифрует символ
        :param letter: символ, который будет зашифрован
        :param index: позиция символа в сообщении
        :param alphabet: алфавит, по которому шифруется символ
        :return: ничего
        """

