from abc import ABC, abstractmethod
from alphabets import *


class ChangeMessage(ABC):
    def __init__(self, message, key):
        self.message = message
        self.key = len(self.message) // len(key) + 1
        self.alphabet_upper_en = alphabet_upper_en
        self.alphabet_lower_en = alphabet_lower_en
        self.changed_message = ''

    def change_message(self):
        for index, letter in enumerate(self.message):
            if letter in self.alphabet_upper_en:
                self.changed_message += self.change_letter(letter, index, self.alphabet_upper_en)
            elif letter in self.alphabet_lower_en:
                self.changed_message += self.change_letter(letter, index, self.alphabet_lower_en)
            else:
                self.changed_message += letter

    @abstractmethod
    def change_letter(self, letter, index, alphabet):
        pass
