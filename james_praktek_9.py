#Nama: James Martyno S
#Kelas: XI TKJ 2
#Nomor Absen: 15
#Soal:Sebagai seorang pengembang perangkat lunak, Anda perlu membuat program sederhana yang menghitung bonus tahunan karyawan berdasarkan performa mereka.

# Input nilai performa karyawan (1-5)
performa = int(input("Masukkan nilai performa karyawan (1-5): "))

# Input gaji tahunan
gaji_tahunan = float(input("Masukkan gaji tahunan: "))

# Menggunakan percabangan ternary untuk menghitung bonus berdasarkan performa
bonus = (0.20 * gaji_tahunan) if performa == 5 else \
        (0.10 * gaji_tahunan) if performa == 4 else \
        (0.05 * gaji_tahunan) if performa == 3 else \
        (0.02 * gaji_tahunan) if performa == 2 else 0

# Mencetak bonus tahunan
print(f"Bonus tahunan: {bonus:.2f} IDR")
