def beaufort_cipher(text, key, mode="e"):
    """Encrypts or decrypts text using the Beaufort cipher.

    Args:
        text (str): The input text.
        key (str): The key used for encryption/decryption.
        mode (str): "e" for encrypt, "d" for decrypt (same operation in Beaufort).

    Returns:
        str: The transformed text.
    """
    text = text.upper()
    key = key.upper()
    key_length = len(key)
    transformed_text = []

    for i, char in enumerate(text):
        if char.isalpha():
            t = ord(char) - ord('A')
            k = ord(key[i % key_length]) - ord('A')
            transformed_char = chr((k - t) % 26 + ord('A'))  # Correct Beaufort formula
            transformed_text.append(transformed_char)
        else:
            transformed_text.append(char)  # Keep spaces, numbers, etc.

    return ''.join(transformed_text)
