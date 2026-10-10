
# Program Pengolahan Data Sederhana menggunakan CSV

import csv

total_nilai = 0
jumlah_mahasiswa = 0

print("=== Data Mahasiswa ===")

with open(
    "data_mahasiswa.csv",
    mode="r",
    newline="",
    encoding="utf-8"
) as file:
    pembaca = csv.DictReader(file)

    for mahasiswa in pembaca:
        nama = mahasiswa["nama"]
        nilai = float(mahasiswa["nilai"])

        print(f"Nama: {nama}, Nilai: {nilai:g}")

        total_nilai += nilai
        jumlah_mahasiswa += 1

print("\n=== Ringkasan Data ===")

if jumlah_mahasiswa > 0:
    rata_rata = total_nilai / jumlah_mahasiswa

    print("Jumlah mahasiswa:", jumlah_mahasiswa)
    print("Total nilai:", total_nilai)
    print("Rata-rata nilai:", round(rata_rata, 2))
else:
    print("Tidak ada data mahasiswa.")
