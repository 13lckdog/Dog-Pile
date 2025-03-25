from ciphers.sub_lib import substitution_alphabets

def substitution(text, key, mode):
    # Retrieve the appropriate substitution alphabet
    alphabet = substitution_alphabets.get(key)

    if not alphabet:
        raise ValueError(f"Invalid substitution alphabet key: {key}")

    # Reverse the alphabet dictionary for decryption
    reverse_alphabet = {v: k for k, v in alphabet.items()}

    result = []
    for char in text:
        if mode == 'e':
            result.append(alphabet.get(char.upper(), char))  # Encrypt
        elif mode == 'd':
            result.append(reverse_alphabet.get(char, char))  # Decrypt
        else:
            raise ValueError(f"Invalid mode: {mode}")

    return ''.join(result)
