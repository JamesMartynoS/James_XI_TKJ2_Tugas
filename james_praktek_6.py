#Nama: James Martyno S
#Kelas: XI TKJ 2
#Nomor Absen: 15
#Soal: Sebagai seorang administrator sistem, Anda perlu memutuskan apakah suatu sistem perlu di-restart setelah pembaruan perangkat lunak.

# Mengambil informasi pembaruan perangkat lunak dari pengguna (menggunakan 'y' untuk ya, 'n' untuk tidak)
pembaruan_perlukan = input("Apakah sistem memerlukan pembaruan yang memerlukan restart? (y/n): ")

# Memeriksa apakah sistem perlu di-restart
if pembaruan_perlukan.lower() == 'y':
    print("Sistem perlu di-restart.")
else:
    print("Sistem tidak perlu di-restart.")
