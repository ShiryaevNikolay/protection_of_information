import os
import signal
from ciphers.rot13.decrypt.decrypt import Decryption
from ciphers.rot13.encrypt.encrypt import Encryption


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

answers = {
    "Зашифровать": 1,
    "Расшифровать": 2
}

# Ввод пользователя:
# Выбираем, что делать с сообщением: зашифровать/расшифровать
print("Выберите, что нужно сделать с сообщением:")
print("{answer} {encrypt}".format(answer=answers.get("Зашифровать"), encrypt=list(answers.keys())[0]))
print("{answer} {decrypt}".format(answer=answers.get("Расшифровать"), decrypt=list(answers.keys())[1]))
while True:
    try:
        selected_answer = int(input("Ответ: "))
        if selected_answer in answers.values():
            break
        else:
            print("Введите", end=" ")
            for index, value in enumerate(answers.values()):
                if index == len(answers.values()) - 1:
                    print(value)
                    break
                print(value, end=', ')
    except:
        print("Неверный ввод")

# Ввод сообщения
message = input("Введите сообщение, которое нужно зашифровать: ")

# Изменяет сообщение
if selected_answer == answers["Зашифровать"]:
    show_change_message(Encryption(message))
elif selected_answer == answers["Расшифровать"]:
    show_change_message(Decryption(message))
