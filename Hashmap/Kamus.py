import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QTextEdit, QInputDialog, QFormLayout
from googletrans import Translator

class AddWordDialog(QDialog):
    def __init__(self, parent=None):
        super(AddWordDialog, self).__init__(parent)

        self.word_en_label = QLabel("Kata dalam Bahasa Inggris:", self)
        self.word_en_input = QLineEdit(self)

        self.word_id_label = QLabel("Kata dalam Bahasa Indonesia:", self)
        self.word_id_input = QLineEdit(self)

        layout = QFormLayout()
        layout.addRow(self.word_en_label, self.word_en_input)
        layout.addRow(self.word_id_label, self.word_id_input)
        layout.addRow(self.addButton)

        self.setLayout(layout)

    def get_words(self):
        return self.word_en_input.text(), self.word_id_input.text()

class DictionaryGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kamus")
        self.setGeometry(100, 100, 450, 600)

        self.initUI()

    def initUI(self):
        self.translate_to_eng_button = QPushButton("Terjemahkan ke Inggris", self)
        self.translate_to_eng_button.setGeometry(10, 50, 200, 30)
        self.translate_to_eng_button.clicked.connect(self.translate_to_english)

        self.translate_to_ind_button = QPushButton("Terjemahkan ke Indonesia", self)
        self.translate_to_ind_button.setGeometry(220, 50, 200, 30)
        self.translate_to_ind_button.clicked.connect(self.translate_to_indonesian)

        self.exit_button = QPushButton("Keluar", self)
        self.exit_button.setGeometry(10, 540, 80, 30)
        self.exit_button.clicked.connect(self.close)

        self.result_text = QTextEdit(self)
        self.result_text.setGeometry(10, 90, 780, 450)
        self.result_text.setReadOnly(True)

    def show_input_dialog(self, prompt):  
        text, okPressed = QInputDialog.getText(self, "Input", prompt)
        if okPressed and text != '':
            return text
        return None

    def translate_to_english(self):
        word = self.show_input_dialog("Masukkan kata untuk diterjemahkan ke Inggris:")
        if word:
            translator = Translator()
            translation = translator.translate(word, src='id', dest='en').text
            self.result_text.append(f'Terjemahan dari "{word}" ke Inggris: {translation}')
        else:
            self.result_text.append('Input tidak valid')

    def translate_to_indonesian(self):
        word = self.show_input_dialog("Masukkan kata untuk diterjemahkan ke Indonesia:")
        if word:
            translator = Translator()
            translation = translator.translate(word, src='en', dest='id').text
            self.result_text.append(f'Terjemahan dari "{word}" ke Indonesia: {translation}')
        else:
            self.result_text.append('Input tidak valid')

def main():
    app = QApplication(sys.argv)
    window = DictionaryGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
