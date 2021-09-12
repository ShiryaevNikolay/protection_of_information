import os
import signal
from cipher_caesar import cipher_caesar_encrypt

signal.signal(signal.SIGINT, lambda *_: os._exit(1))  # Для корректного выхода из программы

answers = [1, 2]

print("Выберите, что нужно сделать с сообщением:")
print("{encrypt} Зашифровать".format(encrypt=answers[0]))
print("{decrypt} Расшифровать".format(decrypt=answers[1]))
while True:
    try:
        select = int(input("Ответ: "))
        if select in answers:
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

message = input("Введите сообщение, которое нужно зашифровать: ")

while True:
    try:
        key = int(input("Введите ключ: "))
        break
    except:
        print("Неверный ввод")

encrypted_message = cipher_caesar_encrypt(message, key)

print("Исходное сообщение: {message}".format(message=message))
print("Зашифрованное сообщение: {message}".format(message=encrypted_message))
