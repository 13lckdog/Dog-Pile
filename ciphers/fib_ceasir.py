import string

def fibonacci_sequence(n):
    """Generate the Fibonacci sequence up to n elements (excluding the initial 0)."""
    fib_seq = [0, 1]
    for _ in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[1:]  # Skip the initial 0

def fib_caesar_cipher(text, key=None, mode="e"):
    """Encrypts or decrypts text using a Fibonacci-based Caesar shift.

    Args:
        text (str): The input text.
        key (None): Unused, but kept for function signature consistency.
        mode (str): "e" for encrypt, "d" for decrypt.

    Returns:
        str: The transformed text.
    """
    text = text.upper()  # Ensure text is in uppercase
    fib_seq = fibonacci_sequence(len(text))  # Generate Fibonacci shifts

    shifted_text = []
    for i, char in enumerate(text):
        if char in string.ascii_uppercase:
            shift = fib_seq[i % len(fib_seq)]
            if mode == "d":
                shift = -shift  # Reverse shift for decryption
            shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            shifted_text.append(shifted_char)
        else:
            shifted_text.append(char)

    return ''.join(shifted_text)
