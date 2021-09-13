from abc import ABC, abstractmethod
from alphabets import *


class ChangeMessage(ABC):

    def __init__(self, message, key):
        """
        Конструктор
        :param message: сообщение, которое нуно изменить
        :param key: ключ, по которому изменяется сообщение
        """
        self.message = message.upper()
        self.key = key.upper() * (len(self.message) // len(key) + 1)
        self.alphabet_upper_en = alphabet_upper_en
        self.matrix_alphabet_upper_en = {}
        self.generate_matrix(self.matrix_alphabet_upper_en, self.alphabet_upper_en)
        self.changed_message = ''

    def change_message(self):
        """
        Функция изменения сообщения
        :return: ничего
        """
        for index, letter in enumerate(self.message):
            if letter in self.alphabet_upper_en:
                self.changed_message += self.change_letter(letter,
                                                           index,
                                                           self.alphabet_upper_en,
                                                           self.matrix_alphabet_upper_en)
            else:
                self.changed_message += letter

    def generate_matrix(self, matrix, alphabet):
        """
        Функция, которая генерирует матрицу алфавита
        :param matrix: матрица, по которой будет шифроваться сообщение
        :param alphabet: алфавит, по которому строится матрица
        :return: ничего
        """
        alphabet_size = len(alphabet)
        for i in range(alphabet_size):
            matrix[alphabet[i]] = []
            for j in range(alphabet_size):
                matrix[alphabet[i]].append(alphabet[(i + j) % alphabet_size])

    @abstractmethod
    def change_letter(self, letter, index, alphabet, matrix):
        """
        Функция изменения символа
        :param letter: символ, который нудно изменить
        :param index: позиция в сообщении
        :param alphabet: алфавит, по которому изменяем символ
        :param matrix: матрица, по которой будет зашифрован символ
        :return: ничего
        """
