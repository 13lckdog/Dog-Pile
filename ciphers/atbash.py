import string

def atbash_cipher(text, key=None, mode="e"):  # Key is ignored, but we keep it for consistency
    atbash_alphabet = {char: string.ascii_uppercase[::-1][i] for i, char in enumerate(string.ascii_uppercase)}

    # Convert text to uppercase
    text = text.upper()

    # Apply Atbash cipher
    result = ''.join(atbash_alphabet.get(char, char) for char in text)

    return result
