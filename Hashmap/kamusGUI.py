import tkinter as tk
from tkinter import simpledialog, messagebox
import random

from RedBlackTree import RedBlackTree

class KamusGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Kamus App")

        self.kamus = RedBlackTree()

        self.label = tk.Label(master, text="Menu:")
        self.label.pack()

        self.button1 = tk.Button(master, text="Terjemahkan ke Inggris", command=self.terjemahkan_indonesia_ke_inggris)
        self.button1.pack()

        self.button2 = tk.Button(master, text="Terjemahkan ke Indonesia", command=self.terjemahkan_inggris_ke_indonesia)
        self.button2.pack()

        self.button4 = tk.Button(master, text="Tampilkan Kamus", command=self.tampilkan_kata)
        self.button4.pack()

        self.button5 = tk.Button(master, text="Keluar", command=self.keluar)
        self.button5.pack()

    def terjemahkan_indonesia_ke_inggris(self):
        kata_indonesia = self.show_input_dialog("Masukkan kata dalam bahasa Indonesia:")
        if kata_indonesia:
            # Membuka file KamusGUI.txt
            try:
                with open("KamusGUI.txt", "r") as file:
                    lines = file.readlines()
                    for line in lines:
                        kata, terjemahan = line.strip().split(":")
                        if kata.lower() == kata_indonesia.lower():
                            self.show_message(f"Terjemahan dari '{kata_indonesia}' ke bahasa Inggris: {terjemahan}")
                            self.gimmick()
                            return
            except FileNotFoundError:
                self.gimmick_kata_tidak_ditemukan(kata_indonesia)

    def terjemahkan_inggris_ke_indonesia(self):
        kata_inggris = self.show_input_dialog("Masukkan kata dalam bahasa Inggris:")
        if kata_inggris:
            # Membuka file KamusGUI.txt
            try:
                with open("KamusGUI.txt", "r") as file:
                    lines = file.readlines()
                    for line in lines:
                        kata, terjemahan = line.strip().split(":")
                        if kata.lower() == kata_inggris.lower():
                            self.show_message(f"Terjemahan dari '{kata_inggris}' ke bahasa Indonesia: {terjemahan}")
                            self.gimmick()
                            return
            except FileNotFoundError:
                self.gimmick_kata_tidak_ditemukan(kata_inggris)

    def gimmick_kata_tidak_ditemukan(self, kata):
        result = messagebox.askquestion("Konfirmasi", f"Kata '{kata}' tidak ditemukan dalam kamus. Apakah Anda ingin menambahkan kata dalam kamus?")
        if result == "yes":
            self.tambahkan_kata()
        else:
            self.show_main_menu()

    def tambahkan_kata(self):
        kata = self.show_input_dialog("Masukkan kata dalam bahasa Indonesia:")
        terjemahan = self.show_input_dialog("Masukkan terjemahan dalam bahasa Inggris:")
        if kata and terjemahan:
            self.kamus.insert(kata.lower(), terjemahan.lower())  # Convert to lowercase for case-insensitive matching
            with open("KamusGUI.txt", "a") as file:
                file.write(f"{kata.lower()}:{terjemahan.lower()}\n")  # Convert to lowercase for consistent storage
            self.show_message(f"Kata '{kata}' sudah ditambahkan ke dalam kamus.")

    def tampilkan_kata(self):
        # Membuka file KamusGUI.txt
        try:
            with open("KamusGUI.txt", "r") as file:
                lines = file.readlines()
                if not lines:
                    self.show_message("Kamus masih kosong.")
                else:
                    message = "Isi kamus:\n"
                    for line in lines:
                        kata, terjemahan = line.strip().split(":")
                        message += f"{kata}: {terjemahan}\n"
                    self.show_message(message)
        except FileNotFoundError:
            self.show_message("Kamus belum dibuat.")

    def gimmick(self):
        angka_acak = [random.randint(1, 100) for _ in range(10)]
        self.show_message("Angka acak dari 1 sampai 100: {}".format(angka_acak))

    def show_input_dialog(self, message):
        return simpledialog.askstring("Input", message)

    def show_message(self, message):
        messagebox.showinfo("Info", message)

    def keluar(self):
        result = messagebox.askquestion("Konfirmasi", "Apakah Anda yakin ingin keluar?")
        if result == "yes":
            self.master.destroy()

    def show_main_menu(self):
        self.master.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    lebar = 400
    tinggi = 300
    root.geometry(f"{lebar}x{tinggi}")
    app = KamusGUI(root)
    root.mainloop()
