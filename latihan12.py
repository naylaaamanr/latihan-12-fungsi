# latihan-12-fungsi

import math

# a. Fungsi menghitung luas persegi panjang
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

# b. Fungsi menghitung volume balok
def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

# c. Fungsi menghitung luas lingkaran
def luas_lingkaran(jari_jari):
    return math.pi * (jari_jari ** 2)

# d. Fungsi menghitung volume bola
def volume_bola(jari_jari):
    return (4 / 3) * math.pi * (jari_jari ** 3)

# --- Program Utama (Input & Output) ---
print("=== PROGRAM HITUNG LUAS & VOLUME ===")

# Input untuk persegi panjang & balok
p = float(input("Masukkan panjang : "))
l = float(input("Masukkan lebar   : "))
t = float(input("Masukkan tinggi  : "))

# Input untuk lingkaran & bola
r = float(input("Masukkan jari-jari: "))

print("\n=== HASIL PERHITUNGAN ===")
print(f"a. Luas persegi panjang   = {luas_persegi_panjang(p, l):.2f}")
print(f"b. Volume balok = {volume_balok(p, l, t):.2f}")
print(f"c. Luas lingkaran         = {luas_lingkaran(r):.2f}")
print(f"d. Volume bola            = {volume_bola(r):.2f}")
