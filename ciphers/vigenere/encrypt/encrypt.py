from ciphers.vigenere.change_message import ChangeMessage


class Encryption(ChangeMessage):

    def change_letter(self, letter, index, alphabet, matrix):
        """
        Функиця, которая шифрует символ
        :param letter: символ, который будет зашифрован
        :param index: позиция символа в сообщении
        :param alphabet: алфавит, по которому шифруется символ
        :return: ничего
        """
        letter_key = self.key[index]
        letter_index_in_alphabet = alphabet.index(letter)
        return matrix[letter_key][letter_index_in_alphabet]
