#Nama: James Martyno S
#Kelas: XI TKJ 2
#Nomor Absen: 15
#Soal: Sebagai seorang sistem administrator, Anda bertanggung jawab untuk memeriksa apakah suatu file di server sudah ada atau belum sebelum menggantinya.

nama_file = input ("Masukkan nama file")
daftar_file_di_server = ["james", "jamess", "data.txt", "file3.txt"]

if nama_file in daftar_file_di_server:
    print("File sudah ada")
else:
    print("File belum ada")