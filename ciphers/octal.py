def octal(text, mode):
    """Converts text to octal (encryption) or octal to text (decryption)."""
    if not text.strip():
        return ""  # Return empty string if input is empty

    if mode == 'e':  # Encrypt (convert to octal)
        return ' '.join(format(ord(char), 'o') for char in text)

    elif mode == 'd':  # Decrypt (convert octal back to text)
        try:
            return ''.join(chr(int(octal, 8)) for octal in text.split())
        except ValueError:
            return "Invalid Octal Input"  # Handle cases where non-octal values are given

    else:
        return "Invalid Mode"  # Handle incorrect mode inputs
