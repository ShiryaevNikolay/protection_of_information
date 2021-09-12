import os
import signal
from encrypt.encrypt import Encryption
from decrypt.decrypt import Decryption


def show_change_message(cipher):
    """
    Функция, которая изменяет сообщение и печатает результат
    :param cipher: объект, который изменяет сообщение
    :return: ничего
    """
    cipher.change_message()
    print("Исходное сообщение: {message}".format(message=cipher.message))
    print("Изменненное сообщение: {message}".format(message=cipher.changed_message))


signal.signal(signal.SIGINT, lambda *_: os._exit(1))  # Для корректного выхода из программы

answers = [1, 2]

# Ввод пользователя:
# Выбираем, что делать с сообщением: зашифровать/расшифровать
print("Выберите, что нужно сделать с сообщением:")
print("{encrypt} Зашифровать".format(encrypt=answers[0]))
print("{decrypt} Расшифровать".format(decrypt=answers[1]))
while True:
    try:
        selected_answer = int(input("Ответ: "))
        if selected_answer in answers:
            break
        else:
            print("Введите", end=" ")
            for index, value in enumerate(answers):
                if index == len(answers) - 1:
                    print(value)
                    break
                print(value, end=', ')
    except:
        print("Неверный ввод")

# Ввод сообщения
message = input("Введите сообщение, которое нужно зашифровать: ")

# Ввод ключа
while True:
    try:
        key = int(input("Введите ключ: "))
        break
    except:
        print("Неверный ввод")

# Изменяет сообщение
if selected_answer == answers[0]:
    show_change_message(Encryption(message, key))
elif selected_answer == answers[1]:
    show_change_message(Decryption(message, key))
