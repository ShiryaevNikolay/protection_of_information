from alphabets import *


class ChangeMessage:
    def __init__(self, message):
        """
        Конструктор
        :param message: сообщение, которое будет зашифрованно
        """
        self.message = message
        self.alphabet_upper_en = alphabet_upper_en
        self.alphabet_lower_en = alphabet_lower_en
        self.alphabet_upper_ru = alphabet_upper_ru
        self.alphabet_lower_ru = alphabet_lower_ru
        self.digits = digits
        self.changed_message = ''

    def change_message(self):
        """
        Функция, которая шифрует сообщение
        :return: ничего
        """
        for letter in self.message:
            if letter in self.alphabet_upper_en:
                self.changed_message += self.change_letter(letter, self.alphabet_upper_en)
            elif letter in self.alphabet_lower_en:
                self.changed_message += self.change_letter(letter, self.alphabet_lower_en)
            elif letter in self.alphabet_upper_ru:
                self.changed_message += self.change_letter(letter, self.alphabet_upper_ru)
            elif letter in self.alphabet_lower_ru:
                self.changed_message += self.change_letter(letter, self.alphabet_lower_ru)
            elif letter in self.digits:
                self.changed_message += self.change_letter(letter, self.digits)
            else:
                self.changed_message += letter

    def change_letter(self, letter, alphabet):
        """
        Функция, которая шифрует символ
        :param letter: символ, который будет зашифрован
        :param alphabet: алфавит, по которому будет шиброваться символ
        :return: ничего
        """
        max_index = len(alphabet) - 1
        position = alphabet.find(letter)
        new_position = max_index - position
        return alphabet[new_position]
