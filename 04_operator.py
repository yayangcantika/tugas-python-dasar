
# Program Operator Aritmatika

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

print("\n=== Hasil Operasi ===")
print("Penjumlahan:", angka1 + angka2)
print("Pengurangan:", angka1 - angka2)
print("Perkalian:", angka1 * angka2)

if angka2 != 0:
    print("Pembagian:", angka1 / angka2)
else:
    print("Pembagian tidak bisa dilakukan dengan nol.")

print("Sisa bagi:", angka1 % angka2 if angka2 != 0 else "Tidak tersedia")
print("Pangkat:", angka1 ** angka2)
