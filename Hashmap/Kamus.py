import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QWidget

class Dictionary:
    def __init__(self):
        self.words = []

    def add_translation(self, word1, word2):
        self.words.append((word1, word2))

    def translate(self, word, reverse=False):
        translations = []
        for word1, word2 in self.words:
            if (reverse and word2 == word) or (not reverse and word1 == word):
                translations.append(word1 if reverse else word2)
        return translations

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for word1, word2 in self.words:
                file.write(f"{word1} - {word2}\n")

    def load_from_file(self, filename):
        self.words = []
        with open(filename, 'r') as file:
            for line in file:
                translation_parts = line.strip().split("-")
                if len(translation_parts) == 2:
                    word1, word2 = translation_parts
                    self.add_translation(word1.strip(), word2.strip())

class DictionaryGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("English-Indonesian Dictionary")
        self.setGeometry(100, 100, 800, 600)

        self.dictionary = Dictionary()

        self.initUI()

    def initUI(self):
        self.dictionary_name = "Kamus Bahasa Inggris - Indonesia"
        self.status_label = QLabel(self.dictionary_name + " berhasil dimuat!", self)
        self.status_label.setGeometry(10, 10, 500, 30)

        self.insert_word_label = QLabel("Tambah Kata:", self)
        self.insert_word_label.setGeometry(10, 50, 100, 30)

        self.insert_word_input = QLineEdit(self)
        self.insert_word_input.setGeometry(120, 50, 200, 30)

        self.insert_button = QPushButton("Tambah", self)
        self.insert_button.setGeometry(330, 50, 80, 30)
        self.insert_button.clicked.connect(self.insert_word)

        self.lookup_word_label = QLabel("Cari Kata:", self)
        self.lookup_word_label.setGeometry(10, 90, 100, 30)

        self.lookup_word_input = QLineEdit(self)
        self.lookup_word_input.setGeometry(120, 90, 200, 30)

        self.lookup_button = QPushButton("Cari", self)
        self.lookup_button.setGeometry(330, 90, 80, 30)
        self.lookup_button.clicked.connect(self.lookup_word)

        self.result_text = QTextEdit(self)
        self.result_text.setGeometry(10, 130, 780, 400)
        self.result_text.setReadOnly(True)

    def insert_word(self):
        translation = self.insert_word_input.text().strip()
        if translation:
            translation_parts = translation.split("-")
            if len(translation_parts) == 2:
                word1, word2 = translation_parts
                self.dictionary.add_translation(word1.strip(), word2.strip())
                self.result_text.append('"' + word1 + '" dan "' + word2 + '" berhasil ditambahkan ke kamus')
                self.insert_word_input.clear()
            else:
                self.result_text.append('Format input tidak valid. Gunakan format "kata1 - kata2"')
        else:
            self.result_text.append('Input tidak valid')

    def lookup_word(self):
        word = self.lookup_word_input.text().strip()
        if word:
            translations = self.dictionary.translate(word)
            if translations:
                self.result_text.append(f'Terjemahan dari "{word}" adalah: {", ".join(translations)}')
            else:
                self.result_text.append(f'"{word}" tidak ditemukan dalam kamus')

def main():
    app = QApplication(sys.argv)
    window = DictionaryGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
