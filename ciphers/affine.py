def modular_inverse(a, m=26):
    """Finds the modular inverse of a under modulo m (used in decryption)."""
    return pow(a, -1, m)

def affine_cipher(text, key, mode):
    """Encrypts or decrypts text using the Affine cipher.

    Args:
        text (str): The input text (assumed to be preprocessed).
        key (tuple): A tuple (a, b) where 'a' is coprime with 26.
        mode (str): "e" for encrypt, "d" for decrypt.

    Returns:
        str: The transformed text.
    """
    a, b = key  # Extract the two key values
    m = 26
    text = text.upper()
    result_text = []

    if mode == "d":
        a = modular_inverse(a, m)  # Compute modular inverse for decryption
        b = -b  # Negate 'b' for decryption

    for char in text:
        if char.isalpha():
            x = ord(char) - ord('A')
            if mode == "e":
                new_char = (a * x + b) % m  # Encryption formula
            elif mode == "d":
                new_char = (a * (x + b)) % m  # Decryption formula
            else:
                raise ValueError(f"Invalid mode: {mode}")
            result_text.append(chr(new_char + ord('A')))
        else:
            result_text.append(char)  # Preserve non-alphabetic characters

    return ''.join(result_text)
