
# Program Function

def hitung_luas(panjang, lebar):
    return panjang * lebar

def tampilkan_hasil(luas):
    print("Luas persegi panjang:", luas)

print("=== Menghitung Luas Persegi Panjang ===")

panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

hasil = hitung_luas(panjang, lebar)
tampilkan_hasil(hasil)
