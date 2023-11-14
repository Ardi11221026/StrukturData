import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QInputDialog, QMessageBox
import os
import random
from RedBlackTree import RedBlackTree

class KamusGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.kamus = RedBlackTree()

        self.setWindowTitle("Kamus GUI")
        self.setGeometry(100, 100, 400, 300)

        menu_label = QLabel("Menu:", self)
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
        kata_indonesia, ok_pressed = QInputDialog.getText(self, "Terjemahkan ke Inggris", "Masukkan kata dalam bahasa Indonesia:")
        if ok_pressed and kata_indonesia:
            if os.path.isfile("KamusPyQt5.txt"):
                with open("KamusPyQt5.txt", "r") as file:
                    lines = file.readlines()
                for line in lines:
                    kata, terjemahan = line.strip().split(":")
                    if kata.lower() == kata_indonesia.lower():
                        QMessageBox.information(self, "Terjemahan", f"Terjemahan dari '{kata_indonesia}' ke bahasa Inggris: {terjemahan}")
                        self.gimmick()
                        return
                QMessageBox.information(self, "Kata Tidak Ditemukan", f"Kata '{kata_indonesia}' tidak ditemukan dalam kamus.")
            else:
                QMessageBox.information(self, "Kamus Belum Dibuat", "Kamus belum dibuat.")
            self.gimmick_kata_tidak_ditemukan()

    def terjemahkan_inggris_ke_indonesia(self):
        kata_inggris, ok_pressed = QInputDialog.getText(self, "Terjemahkan ke Indonesia", "Masukkan kata dalam bahasa Inggris:")
        if ok_pressed and kata_inggris:
            if os.path.isfile("KamusPyQt5.txt"):
                with open("KamusPyQt5.txt", "r") as file:
                    lines = file.readlines()
                for line in lines:
                    kata, terjemahan = line.strip().split(":")
                    if terjemahan.lower() == kata_inggris.lower():
                        QMessageBox.information(self, "Terjemahan", f"Terjemahan dari '{kata_inggris}' ke bahasa Indonesia: {kata}")
                        self.gimmick()
                        return
                QMessageBox.information(self, "Kata Tidak Ditemukan", f"Kata '{kata_inggris}' tidak ditemukan dalam kamus.")
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
        kata, ok_pressed = QInputDialog.getText(self, "Tambah Kata", "Masukkan kata dalam bahasa Indonesia:")
        terjemahan, ok_pressed_terjemahan = QInputDialog.getText(self, "Tambah Kata", "Masukkan terjemahan dalam bahasa Inggris:")
        if ok_pressed and ok_pressed_terjemahan and kata and terjemahan:
            self.kamus.insert(kata.lower(), terjemahan.lower())
            with open("KamusPyQt5.txt", "a") as file:
                file.write(f"{kata.lower()}:{terjemahan.lower()}\n")
            QMessageBox.information(self, "Kata Ditambahkan", f"Kata '{kata}' sudah ditambahkan ke dalam kamus.")

    def tampilkan_kata(self):
        if not os.path.isfile("KamusPyQt5.txt"):
            QMessageBox.information(self, "Kamus Belum Dibuat", "Kamus belum dibuat.")
        else:
            with open("KamusPyQt5.txt", "r") as file:
                lines = file.readlines()
                if not lines:
                    QMessageBox.information(self, "Kamus Kosong", "Kamus masih kosong.")
                else:
                    kamus_content = " ".join(lines)
                    QMessageBox.information(self, "Kamus", kamus_content)

    def gimmick(self):
        angka_acak = [random.randint(1, 100) for _ in range(10)]
        QMessageBox.information(self, "Angka Acak", f"Angka acak dari 1 sampai 100: {angka_acak}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    kamus_gui = KamusGUI()
    kamus_gui.show()
    sys.exit(app.exec_())
