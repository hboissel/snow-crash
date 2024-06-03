#!/usr/bin/python3

def encrypt_data(data):
    # Ensure input is a string
    if not isinstance(data, str):
        raise ValueError("Input must be a string")

    encrypted_data = ""
    extended_ascii_limit = 256  # There are 256 Extended ASCII characters

    for index, char in enumerate(data):
        # Get the current ASCII value of the character
        current_ascii = ord(char)
        
        # Calculate the new position with wrap-around using modulus
        new_ascii = (current_ascii + index) % extended_ascii_limit
        
        # Convert the new ASCII value back to a character
        encrypted_char = chr(new_ascii)
        encrypted_data += encrypted_char

    return encrypted_data

def decrypt_data(encrypted_data):
    # Ensure input is a string
    if not isinstance(encrypted_data, str):
        raise ValueError("Input must be a string")

    decrypted_data = ""
    extended_ascii_limit = 256  # There are 256 Extended ASCII characters

    for index, char in enumerate(encrypted_data):
        # Get the current ASCII value of the character
        current_ascii = ord(char)
        
        # Calculate the original ASCII value, adjusting for wrap-around using modulus
        original_ascii = (current_ascii - index) % extended_ascii_limit
        
        # Convert the ASCII value back to a character
        decrypted_char = chr(original_ascii)
        decrypted_data += decrypted_char

    return decrypted_data

# Example usage:
input_data = "\x66\x34\x6b\x6d\x6d\x36\x70\x7c\x3d\x82\x7f\x70\x82\x6e\x83\x82\x44\x42\x83\x44\x75\x7b\x7f\x8c\x89"
print("Original:", input_data)

decrypted = decrypt_data(input_data)
print("Decrypted:", decrypted)

