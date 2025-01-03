import numpy as np
import string

def autokey_encryption(plain_text, initial_cipher_key):
    """
    Encrypts the given plain text using the Autokey cipher method.

    Args:
        plain_text (str): The text to be encrypted.
        initial_cipher_key (int): The initial key for encryption (0-25).

    Returns:
        str: The encrypted cipher text.
    """
    # Initialize the alphabet and prepare lists for indices and ciphertext
    alpha = list(string.ascii_lowercase)
    plain_index = []  # Stores the index values of the plain text characters
    cipher_key = [initial_cipher_key]  # Start cipher key with the initial value
    cipher_text = []  # To hold the final encrypted text

    # Convert plain text characters to their corresponding index values (0-25)
    for char in plain_text:
        if char != ' ':  # Ignore spaces
            plain_index.append(ord(char) - 97)  # 'a' is 97 in ASCII

    # Build the cipher key by extending it with the indices of the plain text
    cipher_key.extend(plain_index)

    # Encrypt each character using the Autokey cipher algorithm
    for i in range(len(plain_index)):
        # Calculate the cipher index using modular arithmetic
        cipher_index = (plain_index[i] + cipher_key[i]) % 26
        # Convert the cipher index back to a character and append to cipher_text
        cipher_text.append(chr(cipher_index + 97))  # Convert back to char

    return ''.join(cipher_text)  # Join list into a single string and return

def autokey_decryption(cipher_text, initial_cipher_key):
    """
    Decrypts the given cipher text using the Autokey cipher method.

    Args:
        cipher_text (str): The text to be decrypted.
        initial_cipher_key (int): The initial key for decryption (0-25).

    Returns:
        str: The decrypted plain text.
    """
    # Initialize the alphabet and prepare lists for indices and plain text
    alpha = list(string.ascii_lowercase)
    cipher_index = []  # Stores the index values of the cipher text characters
    cipher_key = [initial_cipher_key]  # Start cipher key with the initial value
    plain_text = []  # To hold the final decrypted text

    # Convert cipher text characters to their corresponding index values (0-25)
    for char in cipher_text:
        if char != ' ':  # Ignore spaces
            cipher_index.append(ord(char) - 97)  # 'a' is 97 in ASCII

    # Decrypt each character using the Autokey cipher algorithm
    for j in range(len(cipher_index)):
        # Calculate the plain index using modular arithmetic
        plain_index = (cipher_index[j] - cipher_key[j]) % 26
        # Convert the plain index back to a character and append to plain_text
        plain_text.append(chr(plain_index + 97))  # Convert back to char
        # Update cipher key with the decrypted character index for the next character
        cipher_key.append(plain_index)

    return ''.join(plain_text)  # Join list into a single string and return

def get_key_input():
    """
    Prompts the user for a key input and validates it.

    Returns:
        int: A valid key between 0 and 25.
    """
    while True:
        try:
            key = int(input("Enter your key (0-25):\n"))  # Prompt user for key input
            if 0 <= key <= 25:  # Check if the key is within valid range
                return key  # Return valid key
            else:
                print("Key must be between 0 and 25. Please try again.")  # Prompt for valid key
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 25.")  # Handle non-integer input

def main():
    """
    Main function to run the Autokey cipher program: either encryption or decryption.
    """
    choice = input("Autokey encryption or decryption? (Type 'encryption' or 'decryption')\n").strip().lower()
    
    if choice == "encryption":
        plain_text = input("Enter your plain text:\n").strip().lower()  # Get plain text input
        initial_cipher_key = get_key_input()  # Get and validate the key input
        cipher_text = autokey_encryption(plain_text, initial_cipher_key)  # Encrypt the text
        print("Encrypted text:", cipher_text)  # Output the encrypted text
        
    elif choice == "decryption":
        cipher_text = input("Enter your cipher text:\n").strip().lower()  # Get cipher text input
        initial_cipher_key = get_key_input()  # Get and validate the key input
        decrypted_text = autokey_decryption(cipher_text, initial_cipher_key)  # Decrypt the text
        print("Decrypted text:", decrypted_text)  # Output the decrypted text
        
    else:
        print("Invalid choice. Please type 'encryption' or 'decryption'.")  # Handle invalid options

if __name__ == "__main__":
    main()  # Execute the main function when the script runs