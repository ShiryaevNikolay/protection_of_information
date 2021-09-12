from abc import ABC, abstractmethod
from alphabets import *


class ChangeMessage(ABC):

    def __init__(self, message, key=3):
        """
        Конструктор
        :param message: сообщение, которое нужно изменить
        :param key: ключ
        """
        self.message = message
        self.key = key
        self.alphabet_upper_en = alphabet_upper_en
        self.alphabet_lower_en = alphabet_lower_en
        self.alphabet_upper_ru = alphabet_upper_ru
        self.alphabet_lower_ru = alphabet_lower_ru
        self.digits = digits
        self.changed_message = ''

    def change_message(self):
        """
        Функция изменения сообщения
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

    @abstractmethod
    def change_letter(self, letter, alphabet):
        """
        Изменение символа
        :param letter: символ, который нужно изменить
        :param alphabet: алфавит, по которому меняем символ
        :return: измененный символ
        """
