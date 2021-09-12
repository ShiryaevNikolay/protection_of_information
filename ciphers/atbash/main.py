from change_message import ChangeMessage


def show_changed_message(cipher):
    """
    Функция, которая шибрует сообщение и печатает результат
    :param cipher: объект, которая содержит алгорит шифрования
    :return: ничего
    """
    cipher.change_message()
    print("Исходное сообщение: {message}".format(message=cipher.message))
    print("Изменненное сообщение: {message}".format(message=cipher.changed_message))


# Ввод сообщения
message = input("Введите сообщение, которое нужно зашифровать: ")

show_changed_message(ChangeMessage(message))
