from cipher_caesar import cipher_caesar_encrypt

message = input("Введите сообщение, которое нужно зашифровать: ")
key = int(input("Введите ключ: "))

encrypted_message = cipher_caesar_encrypt(message, key)

print("Исходное сообщение: {message}".format(message=message))
print("Зашифрованное сообщение: {message}".format(message=encrypted_message))
