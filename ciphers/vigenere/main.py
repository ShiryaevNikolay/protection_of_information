from change_message import ChangeMessage


def show_changed_message(cipher):
    """
    Функция, которая изменяет сообщение и печатает результат
    :param cipher: объект, который изменяет сообщение
    :return: ничего
    """
    cipher.change_message()
    print("Исходное сообщение: {message}".format(message=cipher.message))
    print("Изменненное сообщение: {message}".format(message=cipher.changed_message))


# Ввод сообщения
message = input("Введите сообщение, которое нужно зашифровать: ")

# Ввод текста ключа
key = input("Введите текст ключа: ")
