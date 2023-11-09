#Nama           : James Martyno S
#Kelas          : XI TKJ 2
#Nomor Absen    : 15
#Soal           : Buatlah sebuah fungsi yang menghitung total dari deret bilangan ganjil hingga batas tertentu yang ditentukan pengguna

def total_deret_ganjil(batas):
    total = 0
    for i in range(1, 2*batas, 2):
        total += i
    return total

batas_pengguna = int(input("Masukkan batas deret ganjil: "))
hasil_total = total_deret_ganjil(batas_pengguna)
print("Total deret bilangan ganjil hingga batas {batas_pengguna} adalah: {hasil_total}")