def encode_to_binary(message):
    # Кодер: строка -> ascii -> двоичная система
    unicode_encoded = [bin(ord(char))[2:].zfill(16) for char in message]
    # преобразуем список двоичных чисел в одну строку
    binary_string = ''.join(unicode_encoded)
    return binary_string

def decode_to_string(binary_string):
    # Декодер: двоичная система -> ascii -> строка
    unicode_chars = [binary_string[i:i+16] for i in range(0, len(binary_string), 16)]
    decoded_message = ''.join([chr(int(char, 2)) for char in unicode_chars])
    return decoded_message

# Пример использования:
message = "Привет, мир!"
encoded_message = encode_to_binary(message)
print("Закодированное сообщение:", encoded_message)

decoded_message = decode_to_string(encoded_message)
print("Декодированное сообщение:", decoded_message)
