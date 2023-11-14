import os
import random

from RedBlackTree import RedBlackTree

class KamusCLI:
    def __init__(self):
        self.kamus = RedBlackTree()

    def terjemahkan_indonesia_ke_inggris(self):
        kata_indonesia = input("Masukkan kata dalam bahasa Indonesia: ")
        if kata_indonesia:
            if os.path.isfile("KamusCLI.txt"):
                with open("KamusCLI.txt", "r") as file:
                    lines = file.readlines()
                for line in lines:
                    kata, terjemahan = line.strip().split(" : ")
                    if kata.lower() == kata_indonesia.lower():
                        print(f"Terjemahan dari '{kata_indonesia}' ke bahasa Inggris: {terjemahan}")
                        self.gimmick()
                        return
                print(f"Kata '{kata_indonesia}' tidak ditemukan dalam kamus.")
            else:
                print("Kamus belum dibuat.")
            self.gimmick_kata_tidak_ditemukan()

    def terjemahkan_inggris_ke_indonesia(self):
        kata_inggris = input("Masukkan kata dalam bahasa Inggris: ")
        if kata_inggris:
            if os.path.isfile("KamusCLI.txt"):
                with open("KamusCLI.txt", "r") as file:
                    lines = file.readlines()
                for line in lines:
                    kata, terjemahan = line.strip().split(" : ")
                    if terjemahan.lower() == kata_inggris.lower():
                        print(f"Terjemahan dari '{kata_inggris}' ke bahasa Indonesia: {kata}")
                        self.gimmick()
                        return
                print(f"Kata '{kata_inggris}' tidak ditemukan dalam kamus.")
            else:
                print("Kamus belum dibuat.")
            self.gimmick_kata_tidak_ditemukan()

    def gimmick_kata_tidak_ditemukan(self):
        print("Apakah Anda ingin menambahkan kata ke dalam kamus?")
        tambah_kata = input("Masukkan 'y' untuk menambahkan, atau 'n' untuk keluar: ")
        if tambah_kata.lower() == 'y':
            self.tambahkan_kata()
        else:
            print("Terima kasih!")

    def tambahkan_kata(self):
        kata = input("Masukkan kata dalam bahasa Indonesia: ")
        terjemahan = input("Masukkan terjemahan dalam bahasa Inggris: ")
        if kata and terjemahan:
            self.kamus.insert(kata.lower(), terjemahan.lower())
            with open("KamusCLI.txt", "a") as file:
                file.write(f"{kata.lower()} : {terjemahan.lower()}\n")
            print(f"Kata '{kata}' sudah ditambahkan ke dalam kamus.")

    def tampilkan_kata(self):
        if not os.path.isfile("KamusCLI.txt"):
            print("Kamus belum dibuat.")
        else:
            with open("KamusCLI.txt", "r") as file:
                lines = file.readlines()
                if not lines:
                    print("Kamus masih kosong.")
                else:
                    print("Isi kamus:")
                    for line in lines:
                        kata, terjemahan = line.strip().split(" : ")
                        print(f"{kata} : {terjemahan}")

    def gimmick(self):
        angka_acak = [random.randint(1, 100) for _ in range(10)]
        print("Angka acak dari 1 sampai 100:", angka_acak)

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Terjemahkan ke Inggris")
            print("2. Terjemahkan ke Indonesia")
            print("3. Tampilkan Kamus")
            print("4. Keluar")

            choice = input("Pilih menu (1-5): ")

            if choice == "1":
                self.terjemahkan_indonesia_ke_inggris()
            elif choice == "2":
                self.terjemahkan_inggris_ke_indonesia()
            elif choice == "3":
                self.tampilkan_kata()
            elif choice == "4":
                break
            else:
                print("Pilihan tidak valid. Silakan pilih antara 1-5.")

if __name__ == "__main__":
    kamus_cli = KamusCLI()
    kamus_cli.run()
