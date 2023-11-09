#Nama           : James Martyno S
#Kelas          : XI TKJ 2
#Nomor Absen    : 15
#Soal : Buatlah sebuah fungsi untuk menghitung jumlah digit dari suatu bilangan.

def jumlah_digit(bil):
    bil_str = str(bil)

    jumlah_digit = 0
    for digit in bil_str:
        if digit.isdigit():
            jumlah_digit += int(digit)

    return jumlah_digit

bil = int(input("Masukkan bilangan: "))
hasil = jumlah_digit(bil)
print(f'jumlah digit dari {bil} adalah {hasil}')