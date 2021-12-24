import os
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305

"""
Конструкция ChaCha20Poly1305 определена в разделе 2.8 RFC 7539. 
Это потоковый шифр в сочетании с MAC, который предлагает надежные гарантии целостности.
"""

input_value = input('Введите текст, который нужно зашифровать: ')

# Преобразовываем введенный текст в байты
data = bytes(input_value, encoding='utf-8')

aad = bytes("аутентифицированные, но незашифрованные данные", encoding='utf-8')

'''
Безопасно генерирует случайный ключ ChaCha20Poly1305.
Возвращает 32-байтовый ключ.
'''
key = ChaCha20Poly1305.generate_key()

chacha = ChaCha20Poly1305(key)
nonce = os.urandom(12)

'''
encrypt(nonce, data, associated_data)
Шифрует предоставленные data и аутентифицирует associated_data. 
Результат этого может быть передан непосредственно методу дешифрования decrypt().
Параметры:
- nonce (байтовый) - 12-байтовое значение. НИКОГДА НЕ ИСПОЛЬЗУЙТЕ NONCE повторно с ключом.
- data (bytes) – Данные для шифрования.
- associated_data (bytes) - Дополнительные данные, которые должны быть аутентифицированы с помощью ключа, 
но не нуждаются в шифровании. Опционально.
Возвращает байты: Байты зашифрованного текста с добавленным 16-байтовым тегом.
'''
encrypt_text = chacha.encrypt(nonce, data, aad)
print('Зашифрованный текст: ', encrypt_text)

'''
decrypt(nonce, data, associated_data)
Расшифровывает data и аутентифицирует associated_data. 
Если вы вызвали encrypt с associated_data, вы должны передать те же associated_data при расшифровке, 
иначе проверка целостности не удастся.
Возвращает байты: Исходный открытый текст.
'''
decrypt_text = chacha.decrypt(nonce, encrypt_text, aad)
print('Расшифрованный текст: ', decrypt_text)
