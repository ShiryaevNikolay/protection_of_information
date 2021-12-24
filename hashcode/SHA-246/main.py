from hashlib import sha256

'''
Вводим текст, у которого нужно получить хэш-код
'''
input_value = input('Введите текст, у которого нужно получить хэш-код: ')

'''
Чтобы предоставить строку для вычисления хэша,
ее следует закодировать с помощью функции encode()
'''
encoded_message = input_value.encode('utf-8')

'''
Вычисляем хэш-код с помощью функции SHA-256
'''
hash_value = sha256(encoded_message)

'''
Выводим в консоль вычисленный хэш-код 
в шестнацетиричном формате с помощью функции hexdigest()
'''
print('Хэш-код введенного текста: ', hash_value.hexdigest())
