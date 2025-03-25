import string

def caesar_cipher(text, key, mode="e"):
    """Encrypts or decrypts text using a Caesar shift.

    Args:
        text (str): The input text.
        key (int): The shift value.
        mode (str): "e" for encrypt, "d" for decrypt.

    Returns:
        str: The transformed text.
    """
    shift = int(key)  # Ensure key is an integer

    if mode == "d":
        shift = -shift  # Reverse shift for decryption

    shifted_text = []
    for char in text.upper():
        if char in string.ascii_uppercase:
            shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            shifted_text.append(shifted_char)
        else:
            shifted_text.append(char)

    return ''.join(shifted_text)
