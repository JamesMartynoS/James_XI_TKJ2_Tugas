#Nama: James Martyno S
#Kelas: XI TKJ 2
#Nomor Absen: 15
#Soal: Sebagai seorang manajer proyek, Anda perlu menentukan apakah suatu proyek akan diluncurkan atau ditunda berdasarkan status persiapan.

status_persiapan = input("Masukkan status persiapan proyek (Siap/Tunda): ")

if status_persiapan.lower() == "siap":
    print("Proyek diluncurkan.")
elif status_persiapan.lower() == "tunda":
    print("Proyek ditunda.")
else:
    print("Status persiapan tidak valid. Harap masukkan 'Siap' atau 'Tunda'.")
