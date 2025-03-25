import re

def playfair(text, key, mode):
    """Encrypts or decrypts using the Playfair cipher with a 6x6 grid (A-Z, 0-9)."""

    def generate_matrix(key):
        """Generates a 6x6 matrix from the provided key."""
        key = key.upper().replace("J", "I")  # Convert 'J' to 'I'
        seen = set()
        matrix = []

        # Add key characters first
        for char in key:
            if char not in seen and char.isalnum():
                seen.add(char)
                matrix.append(char)

        # Add remaining letters & digits
        for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ0123456789":
            if char not in seen:
                seen.add(char)
                matrix.append(char)

        return [matrix[i:i+6] for i in range(0, 36, 6)]

    def format_text(text, mode):
        """Formats text into digraphs, inserting 'X' where needed."""
        text = re.sub(r'[^A-Z0-9]', '', text.upper().replace("J", "I"))  # Keep only valid characters
        formatted_text = []

        if mode == 'e':  # Encryption formatting
            i = 0
            while i < len(text):
                if i == len(text) - 1:
                    formatted_text.append(text[i] + 'X')  # Pad last letter with 'X'
                    break
                elif text[i] == text[i + 1]:
                    formatted_text.append(text[i] + 'X')  # Insert 'X' between doubles
                    i += 1
                else:
                    formatted_text.append(text[i] + text[i + 1])
                    i += 2
        else:  # Decryption formatting (keep pairs)
            formatted_text = [text[i:i+2] for i in range(0, len(text), 2)]

        return formatted_text

    def find_position(matrix, char):
        """Finds the (row, col) of a character in the matrix."""
        for r, row in enumerate(matrix):
            if char in row:
                return r, row.index(char)
        return None

    # Generate Playfair matrix
    matrix = generate_matrix(key)
    formatted_text = format_text(text, mode)
    result = []

    for pair in formatted_text:
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])

        if row1 is None or row2 is None:
            continue  # Skip invalid characters

        if row1 == row2:  # Same row → shift right (encrypt) / left (decrypt)
            if mode == 'e':
                result.append(matrix[row1][(col1 + 1) % 6] + matrix[row2][(col2 + 1) % 6])
            else:
                result.append(matrix[row1][(col1 - 1) % 6] + matrix[row2][(col2 - 1) % 6])

        elif col1 == col2:  # Same column → shift down (encrypt) / up (decrypt)
            if mode == 'e':
                result.append(matrix[(row1 + 1) % 6][col1] + matrix[(row2 + 1) % 6][col2])
            else:
                result.append(matrix[(row1 - 1) % 6][col1] + matrix[(row2 - 1) % 6][col2])

        else:  # Rectangle swap
            result.append(matrix[row1][col2] + matrix[row2][col1])

    final_text = ''.join(result)

    if mode == 'd':
        final_text = re.sub(r'X(?=[A-Z0-9])', '', final_text)  # Remove extra X if not at end

    return final_text
