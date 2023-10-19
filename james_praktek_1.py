#Nama: James Martyno S
#Kelas: XI TKJ 2
#Nomor Absen: 15
#Soal: Sebagai seorang manajer proyek, Anda harus menentukan apakah suatu proyek akan selesai tepat waktu atau terlambat.

from datetime import datetime

# Masukkan Tanggal
estimasi_selesai = input("Masukkan estimasi waktu selesai (YYYY-MM-DD): ")
tanggal_target = input("Masukkan tanggal target selesai (YYYY-MM-DD): ")

estimasi_selesai = datetime.strptime(estimasi_selesai, "%Y-%m-%d")
tanggal_target = datetime.strptime(tanggal_target, "%Y-%m-%d")

if estimasi_selesai <= tanggal_target:
    print("Tepat waktu")
else:
    print("Terlambat")
