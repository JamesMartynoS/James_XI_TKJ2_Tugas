#Nama           : James Martyno S
#Kelas          : XI TKJ 2
#Nomor Absen    : 15
#Soal           : Buatlah sebuah fungsi yang menghitung nilai pangkat dari suatu bilangan dengan eksponen tertentu.

def total_deret_bilangan_ganjil(batas):
    total = 0
    for i in range(1, 2*batas, 2):
        total += i
    return total

batas = int(input("Masukkan batas deret bilangan ganjil: "))
hasil = total_deret_bilangan_ganjil(batas)
print(f"Total deret bilangan ganjil hingga batas {batas} adalah {hasil}")