
# Program Percabangan if, elif, dan else

nilai = float(input("Masukkan nilai (0-100): "))

if nilai < 0 or nilai > 100:
    print("Nilai tidak valid.")
elif nilai >= 85:
    print("Nilai: A")
elif nilai >= 75:
    print("Nilai: B")
elif nilai >= 65:
    print("Nilai: C")
elif nilai >= 50:
    print("Nilai: D")
else:
    print("Nilai: E")
