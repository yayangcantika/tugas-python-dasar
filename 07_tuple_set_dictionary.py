
# Program Tuple, Set, dan Dictionary

# Tuple
buah_tuple = ("Apel", "Jeruk", "Mangga")
print("=== Tuple ===")
print("Semua buah:", buah_tuple)
print("Buah pertama:", buah_tuple[0])

# Set
buah_set = {"Apel", "Jeruk", "Apel", "Mangga"}
print("\n=== Set ===")
print("Buah unik:", buah_set)

# Dictionary
mahasiswa = {
    "nama": "Andi",
    "umur": 20,
    "jurusan": "Sains Data"
}

print("\n=== Dictionary ===")
print("Nama:", mahasiswa["nama"])
print("Umur:", mahasiswa["umur"])
print("Jurusan:", mahasiswa["jurusan"])

# Menambahkan data
mahasiswa["semester"] = 3
print("Data lengkap:", mahasiswa)
