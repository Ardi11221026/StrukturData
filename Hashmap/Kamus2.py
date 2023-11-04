from asyncio import exceptions
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QTextEdit, QInputDialog, QFormLayout, QMessageBox
from googletrans import Translator

class Node:
    def __init__(self, key, word_en, word_id, color, left=None, right=None, parent=None):
        self.key = key
        self.word_en = word_en
        self.word_id = word_id
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, None, None, 'BLACK')
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y

        x.parent = y.parent
        if y.parent == self.NIL:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        x.right = y
        y.parent = x

    def insert(self, key, word_en, word_id):
        new_node = Node(key, word_en, word_id, 'RED')
        self._insert(new_node)

    def _insert(self, z):
        y = self.NIL
        x = self.root

        while x != self.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if y == self.NIL:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        z.left = self.NIL
        z.right = self.NIL
        z.color = 'RED'
        self._insert_fixup(z)

    def _insert_fixup(self, z):
        while z.parent.color == 'RED':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'RED':
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'RED':
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self.left_rotate(z.parent.parent)

        self.root.color = 'BLACK'

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        while node != self.NIL:
            if key == node.key:
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return None

class AddWordDialog(QDialog):
    def __init__(self, tree, parent=None):
        super(AddWordDialog, self).__init__(parent)
        self.tree = tree

        self.word_en_label = QLabel("Kata dalam Bahasa Inggris:", self)
        self.word_en_input = QLineEdit(self)

        self.word_id_label = QLabel("Kata dalam Bahasa Indonesia:", self)
        self.word_id_input = QLineEdit(self)

        self.addButton = QPushButton("Tambah Kata", self)
        self.addButton.clicked.connect(self.add_word)

        layout = QFormLayout()
        layout.addRow(self.word_en_label, self.word_en_input)
        layout.addRow(self.word_id_label, self.word_id_input)
        layout.addRow(self.addButton)

        self.setLayout(layout)

    def add_word(self):
        word_en = self.word_en_input.text()
        word_id = self.word_id_input.text()

        if word_en and word_id:
            key = hash(word_en)
            existing_node = self.tree.search(key)
            if existing_node is None:
                self.tree.insert(key, word_en, word_id)
                self.accept()
            else:
                self.word_en_input.clear()
                self.word_id_input.clear()
                self.word_en_input.setFocus()
                self.show_warning("Kata sudah ada dalam kamus!")
        else:
            self.show_warning("Mohon masukkan kata dalam Bahasa Inggris dan Bahasa Indonesia!")

    def show_warning(self, message):
        QMessageBox.warning(self, "Peringatan", message)

class DictionaryGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kamus")
        self.setGeometry(100, 100, 450, 600)

        self.tree = RedBlackTree()

        self.initUI()

    def initUI(self):
        self.translate_to_eng_button = QPushButton("Indonesia -> Inggris", self)
        self.translate_to_eng_button.setGeometry(10, 50, 200, 30)
        self.translate_to_eng_button.clicked.connect(self.translate_to_english)

        self.translate_to_ind_button = QPushButton("Inggris -> Indonesia", self)
        self.translate_to_ind_button.setGeometry(220, 50, 200, 30)
        self.translate_to_ind_button.clicked.connect(self.translate_to_indonesian)

        self.exit_button = QPushButton("Keluar", self)
        self.exit_button.setGeometry(10, 540, 80, 30)
        self.exit_button.clicked.connect(self.close)

        self.result_text = QTextEdit(self)
        self.result_text.setGeometry(10, 130, 780, 410)
        self.result_text.setReadOnly(True)

    def show_input_dialog(self, prompt):  
        text, okPressed = QInputDialog.getText(self, "Input", prompt)
        if okPressed and text != '':
            return text
        return None

    def translate_to_english(self):
        word = self.show_input_dialog("Masukkan kata untuk diterjemahkan ke Inggris:")
        if word:
            try:
                translator = Translator()
                translation = translator.translate(word, src='id', dest='en').text
                self.result_text.append(f'Terjemahan dari "{word}" ke Inggris: {translation}')
            except exceptions.GoogleTranslateException as e:
                self.result_text.append(f'Error during translation: {str(e)}')
        else:
            self.result_text.append('Input tidak valid')

    def translate_to_indonesian(self):
        word = self.show_input_dialog("Masukkan kata untuk diterjemahkan ke Indonesia:")
        if word:
            try:
                translator = Translator()
                translation = translator.translate(word, src='en', dest='id').text
                self.result_text.append(f'Terjemahan dari "{word}" ke Indonesia: {translation}')
            except exceptions.GoogleTranslateException as e:
                self.result_text.append(f'Error during translation: {str(e)}')
        else:
            self.result_text.append('Input tidak valid')

    def show_add_word_dialog(self):
        dialog = AddWordDialog(self.tree, self)
        dialog.exec_()

def main():
    app = QApplication(sys.argv)
    window = DictionaryGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
