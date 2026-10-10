
# Program Menggunakan Module

import math
import random

angka = float(input("Masukkan angka positif: "))

if angka >= 0:
    print("Akar kuadrat:", math.sqrt(angka))
    print("Pembulatan ke atas:", math.ceil(angka))
    print("Pembulatan ke bawah:", math.floor(angka))
else:
    print("Akar kuadrat tidak dihitung untuk angka negatif.")

angka_acak = random.randint(1, 10)
print("Angka acak:", angka_acak)
