#Nama: James Martyno S
#Kelas: XI TKJ 2
#Nomor Absen: 15
#Soal: Sebagai seorang guru, Anda harus menentukan nilai akhir siswa berdasarkan nilai tugas dan ujian.

# Input nilai tugas dan nilai ujian
nilai_tugas = float(input("Masukkan nilai tugas (skala 0-100): "))
nilai_ujian = float(input("Masukkan nilai ujian (skala 0-100): "))

# Memeriksa apakah siswa lulus atau gagal
if nilai_tugas > 70 and nilai_ujian > 60:
    status = "Lulus"
else:
    status = "Gagal"

# Mencetak nilai akhir siswa
print(f"Hasil: {status}")
