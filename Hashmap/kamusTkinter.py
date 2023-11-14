import tkinter as tk
from tkinter import simpledialog, messagebox
import os
import random
from RedBlackTree import RedBlackTree

class KamusGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.kamus = RedBlackTree()

        self.title("Kamus GUI")
        self.geometry("400x300")

        menu_label = tk.Label(self, text="Menu:")
        menu_label.pack()

        button1 = tk.Button(self, text="Terjemahkan ke Inggris", command=self.terjemahkan_indonesia_ke_inggris)
        button1.pack()

        button2 = tk.Button(self, text="Terjemahkan ke Indonesia", command=self.terjemahkan_inggris_ke_indonesia)
        button2.pack()

        button3 = tk.Button(self, text="Tampilkan Kamus", command=self.tampilkan_kata)
        button3.pack()

        button4 = tk.Button(self, text="Keluar", command=self.destroy)
        button4.pack()

    def terjemahkan_indonesia_ke_inggris(self):
        kata_indonesia = simpledialog.askstring("Terjemahkan ke Inggris", "Masukkan kata dalam bahasa Indonesia:")
        if kata_indonesia:
            if os.path.isfile("KamusTkinter.txt"):
                with open("KamusTkinter.txt", "r") as file:
                    lines = file.readlines()
                for line in lines:
                    kata, terjemahan = line.strip().split(":")
                    if kata.lower() == kata_indonesia.lower():
                        messagebox.showinfo("Terjemahan", f"Terjemahan dari '{kata_indonesia}' ke bahasa Inggris: {terjemahan}")
                        self.gimmick()
                        return
                messagebox.showinfo("Kata Tidak Ditemukan", f"Kata '{kata_indonesia}' tidak ditemukan dalam kamus.")
            else:
                messagebox.showinfo("Kamus Belum Dibuat", "Kamus belum dibuat.")
            self.gimmick_kata_tidak_ditemukan()

    def terjemahkan_inggris_ke_indonesia(self):
        kata_inggris = simpledialog.askstring("Terjemahkan ke Indonesia", "Masukkan kata dalam bahasa Inggris:")
        if kata_inggris:
            if os.path.isfile("KamusTkinter.txt"):
                with open("KamusTkinter.txt", "r") as file:
                    lines = file.readlines()
                for line in lines:
                    kata, terjemahan = line.strip().split(":")
                    if terjemahan.lower() == kata_inggris.lower():
                        messagebox.showinfo("Terjemahan", f"Terjemahan dari '{kata_inggris}' ke bahasa Indonesia: {kata}")
                        self.gimmick()
                        return
                messagebox.showinfo("Kata Tidak Ditemukan", f"Kata '{kata_inggris}' tidak ditemukan dalam kamus.")
            else:
                messagebox.showinfo("Kamus Belum Dibuat", "Kamus belum dibuat.")
            self.gimmick_kata_tidak_ditemukan()

    def gimmick_kata_tidak_ditemukan(self):
        response = messagebox.askquestion("Tambah Kata", "Apakah Anda ingin menambahkan kata ke dalam kamus?")
        if response == 'yes':
            self.tambahkan_kata()
        else:
            messagebox.showinfo("Terima Kasih", "Terima kasih!")

    def tambahkan_kata(self):
        kata = simpledialog.askstring("Tambah Kata", "Masukkan kata dalam bahasa Indonesia:")
        terjemahan = simpledialog.askstring("Tambah Kata", "Masukkan terjemahan dalam bahasa Inggris:")
        if kata and terjemahan:
            self.kamus.insert(kata.lower(), terjemahan.lower())
            with open("KamusTkinter.txt", "a") as file:
                file.write(f"{kata.lower()}:{terjemahan.lower()}\n")
            messagebox.showinfo("Kata Ditambahkan", f"Kata '{kata}' sudah ditambahkan ke dalam kamus.")

    def tampilkan_kata(self):
        if not os.path.isfile("KamusTkinter.txt"):
            messagebox.showinfo("Kamus Belum Dibuat", "Kamus belum dibuat.")
        else:
            with open("KamusTkinter.txt", "r") as file:
                lines = file.readlines()
                if not lines:
                    messagebox.showinfo("Kamus Kosong", "Kamus masih kosong.")
                else:
                    kamus_content = " ".join(lines)
                    messagebox.showinfo("Kamus", kamus_content)

    def gimmick(self):
        angka_acak = [random.randint(1, 100) for _ in range(10)]
        messagebox.showinfo("Angka Acak", f"Angka acak dari 1 sampai 100: {angka_acak}")

if __name__ == "__main__":
    kamus_gui = KamusGUI()
    kamus_gui.mainloop()
