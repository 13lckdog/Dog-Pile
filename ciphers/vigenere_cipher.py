def generate_vigenere_table():
    """Generates a Vigenère cipher table (26x26)."""
    table = []
    for i in range(26):
        row = [chr((i + j) % 26 + ord('A')) for j in range(26)]
        table.append(row)
    return table

def vigenere_cipher(text, key, mode):
    """Encrypts or decrypts text using the Vigenère cipher.

    Args:
        text (str): The input text (assumed to be preprocessed).
        key (str): The encryption key.
        mode (str): "e" for encrypt, "d" for decrypt.

    Returns:
        str: The transformed text.
    """
    table = generate_vigenere_table()
    text = text.upper()
    key = key.upper()
    key_length = len(key)
    result_text = []

    for i in range(len(text)):
        char = text[i]
        key_char = key[i % key_length]

        if char.isalpha():
            row = ord(key_char) - ord('A')
            if mode == "e":
                col = ord(char) - ord('A')
                result_text.append(table[row][col])
            elif mode == "d":
                col = table[row].index(char)
                result_text.append(chr(col + ord('A')))
            else:
                raise ValueError(f"Invalid mode: {mode}")
        else:
            result_text.append(char)  # Keep non-alphabetic characters unchanged

    return ''.join(result_text)
