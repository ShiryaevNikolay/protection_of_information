import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

"""
Конструкция AES-GCM состоит из блочного шифра AES, использующего режим счетчика Галуа (GCM).
"""

input_value = input('Введите текст, который нужно зашифровать: ')

# Преобразовываем введенный текст в байты
data = bytes(input_value, encoding='utf-8')

aad = bytes("аутентифицированные, но незашифрованные данные", encoding='utf-8')

'''
generate_key(bit_length)
Безопасно генерирует случайный ключ AES-GCM.
Параметры: bit_length - Битовая длина ключа для генерации. Должно быть 128, 192 или 256.
Возвращает: Сгенерированный ключ.
'''
key = AESGCM.generate_key(bit_length=128)

aesgcm = AESGCM(key)
nonce = os.urandom(12)

'''
encrypt(nonce, data, associated_data)
Шифрует предоставленные data и аутентифицирует associated_data. 
Результат этого может быть передан непосредственно методу дешифрования decrypt().
Параметры:
- nonce (байтовый) - NIST рекомендует 96-битную длину IV для лучшей производительности, 
но она может составлять до 264 - 1 бит. НИКОГДА НЕ ИСПОЛЬЗУЙТЕ НИКОГДА повторно с ключом.
- data (bytes) – Данные для шифрования.
- associated_data (bytes) - Дополнительные данные, которые должны быть аутентифицированы с помощью ключа, 
но не нуждаются в шифровании. Опционально.
Возвращает байты: Байты зашифрованного текста с добавленным 16-байтовым тегом.
'''
encrypt_text = aesgcm.encrypt(nonce, data, aad)
print('Зашифрованный текст: ', encrypt_text)

'''
decrypt(nonce, data, associated_data)
Расшифровывает data и аутентифицирует associated_data. 
Если вы вызвали encrypt с associated_data, вы должны передать те же associated_data при расшифровке, 
иначе проверка целостности не удастся.
Возвращает байты: Исходный открытый текст.
'''
decrypt_text = aesgcm.decrypt(nonce, encrypt_text, aad)
print('Расшифрованный текст: ', decrypt_text)
