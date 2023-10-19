#Nama: James Martyno S
#Kelas: XI TKJ 2
#Nomor Absen: 15
#Soal: Sebagai seorang kasir di toko, Anda harus menghitung jumlah diskon berdasarkan total belanjaan pelanggan dan jenis anggota (anggota biasa atau anggota premium).

# Input total belanjaan
total_belanjaan = float(input("Masukkan total belanjaan: "))

# Input status anggota (biasa atau premium)
status_anggota = input("Masukkan status anggota (biasa atau premium): ")

# Inisialisasi variabel diskon
diskon = 0

# Memeriksa status anggota dan memberikan diskon sesuai aturan
if status_anggota == "premium":
    if total_belanjaan > 500000:
        diskon = 0.15  # Diskon 15%
    else:
        diskon = 0.10  # Diskon 10%
elif status_anggota == "biasa":
    if total_belanjaan > 300000:
        diskon = 0.07  # Diskon 7%

# Menghitung total belanjaan setelah diskon
total_setelah_diskon = total_belanjaan - (total_belanjaan * diskon)

# Mencetak total belanjaan dan total setelah diskon
print(f"Total belanjaan sebelum diskon: {total_belanjaan:.2f} IDR")
print(f"Total belanjaan setelah diskon: {total_setelah_diskon:.2f} IDR")
