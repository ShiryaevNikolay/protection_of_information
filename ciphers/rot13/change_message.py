from abc import ABC, abstractmethod
from alphabets import *


class ChangeMessage(ABC):

    def __init__(self, message):
        """
        Конструктор
        :param message: сообщение, которое нужно изменить
        """
        self.message = message
        self.alphabet_upper_en = alphabet_upper_en
        self.alphabet_lower_en = alphabet_lower_en
        self.changed_message = ''

    def change_message(self):
        """
        Функция изменения сообщения
        :return:
        """
        for letter in self.message:
            if letter in self.alphabet_upper_en:
                self.changed_message += self.change_letter(letter, self.alphabet_upper_en)
            elif letter in self.alphabet_lower_en:
                self.changed_message += self.change_letter(letter, self.alphabet_lower_en)
            else:
                self.changed_message += letter

    @abstractmethod
    def change_letter(self, letter, alphabet):
        """
        Изменение симола
        :param letter: символ, который будет изменен
        :param alphabet: алфавит, по которому будет изменяться символ
        :return: возвращает измененный символ
        """
