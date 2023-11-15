class Node:
    def __init__(self, key, value, color, left=None, right=None):
        self.key = key
        self.value = value
        self.color = color
        self.left = left
        self.right = right

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, None, "BLACK")
        self.root = self.NIL

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)
        self.root.color = "BLACK"

    def _insert(self, root, key, value):
        if root == self.NIL:
            return Node(key, value, "RED", self.NIL, self.NIL)

        if key < root.key:
            root.left = self._insert(root.left, key, value)
        elif key > root.key:
            root.right = self._insert(root.right, key, value)
        else:
            root.value = value

        if self._is_red(root.right) and not self._is_red(root.left):
            root = self._rotate_left(root)
        if self._is_red(root.left) and self._is_red(root.left.left):
            root = self._rotate_right(root)
        if self._is_red(root.left) and self._is_red(root.right):
            self._flip_colors(root)

        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        while root != self.NIL:
            if key < root.key:
                root = root.left
            elif key > root.key:
                root = root.right
            else:
                return root.value
        return None

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, root, result):
        if root != self.NIL:
            self._inorder_traversal(root.left, result)
            result.append((root.key, root.value))
            self._inorder_traversal(root.right, result)

    def _is_red(self, node):
        return node.color == "RED"

    def _rotate_left(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = "RED"
        return x

    def _rotate_right(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = "RED"
        return x

    def _flip_colors(self, h):
        h.color = "RED"
        h.left.color = "BLACK"
        h.right.color = "BLACK"

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QInputDialog, QMessageBox
import os
import random
from RedBlackTree import RedBlackTree

class KamusGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.kamus = RedBlackTree()

        self.setWindowTitle("Kamus")
        self.setGeometry(100, 100, 400, 300)

        menu_label = QLabel("MENU", self)
        menu_label.move(10, 10)

        button1 = QPushButton("Terjemahkan ke Inggris", self)
        button1.setGeometry(10, 40, 180, 30)
        button1.clicked.connect(self.terjemahkan_indonesia_ke_inggris)

        button2 = QPushButton("Terjemahkan ke Indonesia", self)
        button2.setGeometry(10, 80, 180, 30)
        button2.clicked.connect(self.terjemahkan_inggris_ke_indonesia)

        button3 = QPushButton("Tampilkan Kamus", self)
        button3.setGeometry(10, 120, 180, 30)
        button3.clicked.connect(self.tampilkan_kata)

        button4 = QPushButton("Keluar", self)
        button4.setGeometry(10, 160, 180, 30)
        button4.clicked.connect(self.close)

    def terjemahkan_indonesia_ke_inggris(self):
        key_indonesia, ok_pressed = QInputDialog.getText(self, "Terjemahkan ke Inggris", "Masukkan kata dalam bahasa Indonesia:")
        if ok_pressed and key_indonesia:
            if os.path.isfile("Kamus.txt"):
                with open("Kamus.txt", "r") as file:
                    lines = file.readlines()
                for line in lines:
                    key, value = line.strip().split(" : ")
                    if key.lower() == key_indonesia.lower():
                        QMessageBox.information(self, "Terjemahan", f"Terjemahan dari '{key_indonesia}' ke bahasa Inggris: {value}")
                        self.gimmick(key_indonesia.lower())
                        return
                QMessageBox.information(self, "Kata Tidak Ditemukan", f"Kata '{key_indonesia}' tidak ditemukan dalam kamus.")
                self.gimmick_kata_tidak_ditemukan()
            else:
                QMessageBox.information(self, "Kamus Belum Dibuat", "Kamus belum dibuat.")
                self.gimmick_kata_tidak_ditemukan()

    def terjemahkan_inggris_ke_indonesia(self):
        key_inggris, ok_pressed = QInputDialog.getText(self, "Terjemahkan ke Indonesia", "Masukkan kata dalam bahasa Inggris:")
        if ok_pressed and key_inggris:
            if os.path.isfile("Kamus.txt"):
                with open("Kamus.txt", "r") as file:
                    lines = file.readlines()
                for line in lines:
                    key, value = line.strip().split(" : ")
                    if value.lower() == key_inggris.lower():
                        QMessageBox.information(self, "Terjemahan", f"Terjemahan dari '{key_inggris}' ke bahasa Indonesia: {key}")
                        self.gimmick(key.lower())
                        return
                QMessageBox.information(self, "Kata Tidak Ditemukan", f"Kata '{key_inggris}' tidak ditemukan dalam kamus.")
                self.gimmick_kata_tidak_ditemukan()
            else:
                QMessageBox.information(self, "Kamus Belum Dibuat", "Kamus belum dibuat.")
                self.gimmick_kata_tidak_ditemukan()

    def gimmick_kata_tidak_ditemukan(self):
        response = QMessageBox.question(self, "Tambah Kata", "Apakah Anda ingin menambahkan kata ke dalam kamus?", QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.Yes:
            self.tambahkan_kata()
        else:
            QMessageBox.information(self, "Terima Kasih", "Terima kasih!")

    def tambahkan_kata(self):
        key, ok_pressed = QInputDialog.getText(self, "Tambah Kata", "Masukkan kata dalam bahasa Indonesia:")
        value, ok_pressed_value = QInputDialog.getText(self, "Tambah Kata", "Masukkan terjemahan dalam bahasa Inggris:")
        if ok_pressed and ok_pressed_value and key and value:
            self.kamus.insert(key.lower(), value.lower())
            with open("Kamus.txt", "a") as file:
                file.write(f"{key.lower()} : {value.lower()}\n")
            QMessageBox.information(self, "Kata Ditambahkan", f"Kata '{key}' sudah ditambahkan ke dalam kamus.")

    def tampilkan_kata(self):
        if not os.path.isfile("Kamus.txt"):
            QMessageBox.information(self, "Kamus Belum Dibuat", "Kamus belum dibuat.")
        else:
            with open("Kamus.txt", "r") as file:
                lines = file.readlines()
                if not lines:
                    QMessageBox.information(self, "Kamus Kosong", "Kamus masih kosong.")
                else:
                    kamus_content = " ".join(lines)
                    QMessageBox.information(self, "Kamus", kamus_content)

    def gimmick(self, key):
        if key.lower() == "buah" or key.lower() == "fruit":
            fruit_list = ["apel", "jeruk", "pisang", "anggur", "kiwi", "mangga", "pir", "semangka", "stroberi", "nanas"]
            random_fruits = random.sample(fruit_list, 10)
            QMessageBox.information(self, "Gimmick", f"10 Nama Buah: {', '.join(random_fruits)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    kamus_gui = KamusGUI()
    kamus_gui.show()
    sys.exit(app.exec_())
