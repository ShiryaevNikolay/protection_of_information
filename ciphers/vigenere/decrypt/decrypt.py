from ciphers.vigenere.change_message import ChangeMessage


class Decryption(ChangeMessage):

    def change_letter(self, letter, index, alphabet, matrix):
        """
        Функиця, которая расшифровывает символ
        :param letter: символ, который будет расшифрован
        :param index: позиция символа в сообщении
        :param alphabet: алфавит, по которому расшифровывается символ
        :return: ничего
        """
        letter_key = self.key[index]
        line_letters = matrix[letter_key]
        letter_index_in_line_letters = line_letters.index(letter)
        return alphabet[letter_index_in_line_letters]
