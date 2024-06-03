#!/usr/bin/python3

def encrypt_data(data):

    encrypted_data = ""
    extended_ascii_limit = 256

    for index, char in enumerate(data):
        current_ascii = ord(char)
        new_ascii = (current_ascii + index) % extended_ascii_limit
        encrypted_char = chr(new_ascii)
        encrypted_data += encrypted_char

    return encrypted_data

def decrypt_data(encrypted_data):
    decrypted_data = ""
    extended_ascii_limit = 256

    for index, char in enumerate(encrypted_data):
        current_ascii = ord(char)
        original_ascii = (current_ascii - index) % extended_ascii_limit
        decrypted_char = chr(original_ascii)
        decrypted_data += decrypted_char

    return decrypted_data

input_data = "\x66\x34\x6b\x6d\x6d\x36\x70\x7c\x3d\x82\x7f\x70\x82\x6e\x83\x82\x44\x42\x83\x44\x75\x7b\x7f\x8c\x89"
print("Original:", input_data)

decrypted = decrypt_data(input_data)
print("Decrypted:", decrypted)

