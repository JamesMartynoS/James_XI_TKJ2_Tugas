#Nama: James Martyno S
#Kelas: XI TKJ 2
#Nomor Absen: 15
#Soal: Sebagai seorang pustakawan, Anda perlu menentukan jenis pinjaman buku berdasarkan durasi peminjaman.

durasi_peminjaman = int(input("Masukkan durasi peminjaman buku (dalam hari): "))

# Jenis pinjaman berdasarkan durasi
if durasi_peminjaman <= 7:
    jenis_pinjaman = "Peminjaman Pendek"
elif 7 < durasi_peminjaman <= 30:
    jenis_pinjaman = "Peminjaman Menengah"
else:
    jenis_pinjaman = "Peminjaman Panjang"

# Jenis pinjaman
print(f"Jenis pinjaman: {jenis_pinjaman}")
