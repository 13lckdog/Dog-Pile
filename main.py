import sys
from PyQt6 import QtWidgets

# Import the generated UI file (from LV1.ui converted using pyuic6)
from guisheets.LV1 import Ui_LV1Zyfrz

# Import ciphers (Add more as needed)
from ciphers.ceasar import ceasar_cipher
from ciphers.fibceasar import fib_ceasar_cipher

def load_stylesheet():
    """ Load the QSS stylesheet for application styling. """
    try:
        with open('guisheets/styles.qss', 'r') as f:
            return f.read()
    except FileNotFoundError:
        print("Stylesheet not found. Using default style.")
        return ""

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Load UI from the generated file
        self.ui = Ui_LV1Zyfrz()
        self.ui.setupUi(self)

        # Apply stylesheet
        self.setStyleSheet(load_stylesheet())

        # Connect buttons
        self.ui.ExicuteButton.clicked.connect(self.run_cipher)

    def run_cipher(self):
        plaintext = self.ui.txtInput.toPlainText()
        cipher_choice = self.ui.lstCypher.currentItem().text()
        sub_choice_item = self.ui.lstSubstitution.currentItem()
        sub_choice = sub_choice_item.text() if apply_substitution and sub_choice_item else None

        # Determine the mode based on the selected radio button
        if self.ui.rdoEncrypt.isChecked():
            mode = 'e'
        elif self.ui.rdoDecrypt.isChecked():
            mode = 'd'
        else:
            mode = None  # Handle the case where no radio button is selected

        # Validate input
        if not plaintext.strip():
            self.ui.txtOutput.setPlainText("Error: Input text is empty.")
            return

        try:
            # Select and run the appropriate cipher
            if cipher_choice == 'Ceasir':
                key = 3  # Temporary fixed key for testing
                result = ceasar_cipher(plaintext, key, mode)
            elif cipher_choice == 'Fibonacci Ceasir':
                key = 5  # Example key for Fibonacci Caesar
                result = fib_ceasar_cipher(plaintext, key, mode)
            else:
                result = "Error: Cipher not implemented."


            # Apply substitution if selected (substitution logic to be implemented)
            if apply_substitution:
                result = apply_substitution(result, sub_choice)

            # Display the result
            self.ui.txtOutput.setPlainText(result)
        except Exception as e:
            self.ui.txtOutput.setPlainText(f"Error: {e}")

def apply_substitution(text, sub_choice):
    """ Placeholder for substitution logic. """
    return text

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
