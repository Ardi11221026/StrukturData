import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox, QInputDialog

class RedBlackTree:
    class Node:
        def __init__(self, key, value, color, parent=None, left=None, right=None):
            self.key = key
            self.value = value
            self.color = color
            self.parent = parent
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if not self.root:
            self.root = self.Node(key, value, 'black')
        else:
            self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if key < node.key:
            if node.left:
                self._insert(node.left, key, value)
            else:
                node.left = self.Node(key, value, 'red', parent=node)
                self._fix_insert(node.left)
        elif key > node.key:
            if node.right:
                self._insert(node.right, key, value)
            else:
                node.right = self.Node(key, value, 'red', parent=node)
                self._fix_insert(node.right)
        else:
            node.value = value

    def _fix_insert(self, node):
        while node.parent and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle and uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._rotate_left(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle and uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._rotate_left(node.parent.parent)
        self.root.color = 'black'

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _rotate_right(self, y):
        x = y.left
        y.left = x.right
        if x.right:
            x.right.parent = y
        x.parent = y.parent
        if not y.parent:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node or key == node.key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

class TranslatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.red_black_tree_indo_to_eng = RedBlackTree()
        self.red_black_tree_eng_to_indo = RedBlackTree()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Translator App')
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()

        translate_to_english_btn = QPushButton('Terjemahkan Bahasa Indonesia ke Inggris', self)
        translate_to_english_btn.clicked.connect(self.translate_to_english)
        self.layout.addWidget(translate_to_english_btn)

        translate_to_indonesian_btn = QPushButton('Terjemahkan Bahasa Inggris ke Indonesia', self)
        translate_to_indonesian_btn.clicked.connect(self.translate_to_indonesian)
        self.layout.addWidget(translate_to_indonesian_btn)

        add_word_btn = QPushButton('Tambahkan Kata ke Kamus', self)
        add_word_btn.clicked.connect(self.add_word)
        self.layout.addWidget(add_word_btn)

        show_words_btn = QPushButton('Tampilkan Kata dalam Kamus', self)
        show_words_btn.clicked.connect(self.show_words)
        self.layout.addWidget(show_words_btn)

        exit_btn = QPushButton('Keluar', self)
        exit_btn.clicked.connect(self.close)
        self.layout.addWidget(exit_btn)

        self.setLayout(self.layout)

    def translate_to_english(self):
        key = self.get_user_input('Masukkan kata dalam bahasa Indonesia:')
        value = self.translate_word(key, self.red_black_tree_indo_to_eng)
        if value:
            QMessageBox.information(self, 'Hasil Terjemahan', f'Terjemahan: {value}')
            self.gimmick(key)
        else:
            reply = QMessageBox.question(self, 'Kata Tidak Ditemukan', 'Kata tidak ditemukan. Apakah Anda ingin menambahkannya ke dalam kamus?',
                                         QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.add_word()

    def translate_to_indonesian(self):
        key = self.get_user_input('Masukkan kata dalam bahasa Inggris:')
        value = self.translate_word(key, self.red_black_tree_eng_to_indo)
        if value:
            QMessageBox.information(self, 'Hasil Terjemahan', f'Terjemahan: {value}')
            self.gimmick(key)
        else:
            reply = QMessageBox.question(self, 'Kata Tidak Ditemukan', 'Kata tidak ditemukan. Apakah Anda ingin menambahkannya ke dalam kamus?',
                                         QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.add_word()

    def add_word(self):
        key = self.get_user_input('Masukkan kata:')
        value = self.get_user_input('Masukkan terjemahan:')
        
        self.red_black_tree_indo_to_eng.insert(key, value)
        self.red_black_tree_eng_to_indo.insert(value, key)

        QMessageBox.information(self, 'Sukses', 'Kata berhasil ditambahkan ke dalam kamus.')

    def show_words(self):
        indonesian_words = self.red_black_tree_indo_to_eng.inorder_traversal()
        english_words = self.red_black_tree_eng_to_indo.inorder_traversal()

        result = 'Bahasa Indonesia:\n'
        result += ', '.join(indonesian_words) if indonesian_words else 'Tidak ada kata dalam kamus.'

        result += '\n\nBahasa Inggris:\n'
        result += ', '.join(english_words) if english_words else 'Tidak ada kata dalam kamus.'

        self.show_message_box('Kata dalam Kamus', result)

    def translate_word(self, key, red_black_tree):
        node = red_black_tree.search(key)
        if node:
            return node.value
        else:
            return None

    def gimmick(self, key):
        if key.lower() == "buah" or key.lower() == "fruit":
            fruit_list = ["apel", "jeruk", "pisang", "anggur", "kiwi", "mangga", "pir", "semangka", "stroberi", "nanas"]
            for fruit in fruit_list:
                self.red_black_tree_indo_to_eng.insert(fruit, fruit)
                self.red_black_tree_eng_to_indo.insert(fruit, fruit)
            QMessageBox.information(self, "Gimmick", f"10 Nama Buah: {', '.join(fruit_list)}")
        elif key.lower() == "hewan" or key.lower() == "animal":
            animal_list = ["buaya", "ayam", "sapi", "kambing", "cacing", "naga", "domba", "tawon", "lebah", "semut", "singa", "gajah", "jerapah", "harimau"]
            for animal in animal_list:
                self.red_black_tree_indo_to_eng.insert(animal, animal)
                self.red_black_tree_eng_to_indo.insert(animal, animal)
            QMessageBox.information(self, "Gimmick", f"10 Nama Hewan: {', '.join(animal_list)}")
        elif key.lower() == "gunung" or key.lower() == "mountain":
            mountain_list = ["Bromo", "Kawi", "Dieng", "Sinabung", "Kerinci", "Merapi", "Agung", "Kintamani", "Rinjani", "Semeru", "Jaya Wijaya", "Meratus", "Kelud", "Merbabu"]
            for mountain in mountain_list:
                self.red_black_tree_indo_to_eng.insert(mountain, mountain)
                self.red_black_tree_eng_to_indo.insert(mountain, mountain)
            QMessageBox.information(self, "Gimmick", f"10 Nama Gunung di Indonesia: {', '.join(mountain_list)}")
        elif key.lower() == "merek" or key.lower() == "brand":
            brand_list = ["ESEMKA", "Hot Ways", "Navy Club", "Heiden Heritage", "Advan", "Indofood", "Wings food", "Erigo", "Eager", "Rexus", "Fantech", "Franc Nobel", "KYT", "NHK","NJS","Polygon","Le Minerale"]
            for brand in brand_list:
                self.red_black_tree_indo_to_eng.insert(brand, brand)
                self.red_black_tree_eng_to_indo.insert(brand, brand)
            QMessageBox.information(self, "Gimmick", f"10 Brand Terkenal di Indonesia: {', '.join(brand_list)}")
        elif key.lower() == "mobil" or key.lower() == "car":
            car_list = ["TOYOTA", "DAIHATSU", "WULING", "CHERRY", "NISSAN", "HYUNDAI", "SUZUKI", "HONDA", "BMW", "MERCEDES BENZ", "VW", "VOLVO", "ASTON MARTIN", "FERARRI","Lamborghini","Porsche","Mitsubishi"]
            for car in car_list:
                self.red_black_tree_indo_to_eng.insert(car, car)
                self.red_black_tree_eng_to_indo.insert(car, car)
            QMessageBox.information(self, "Gimmick", f"10 Brand Mobil Terkenal di Indonesia: {', '.join(car_list)}")
    def show_message_box(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

    def get_user_input(self, prompt):
        text, ok = QInputDialog.getText(self, 'Input', prompt)
        if ok:
            return text
        else:
            return None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TranslatorApp()
    window.show()
    sys.exit(app.exec_())
