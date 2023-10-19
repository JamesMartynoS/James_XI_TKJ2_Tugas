#Nama: James Martyno S
#Kelas: XI TKJ 2
#Nomor Absen: 15
#Soal:Sebagai seorang analis data, Anda harus mengkategorikan produk berdasarkan penjualan bulanan.

# Memasukkan data penjualan bulanan produk
penjualan = int(input("Masukkan jumlah penjualan bulanan produk: "))

# Menentukan kategori produk berdasarkan penjualan
if penjualan > 1000:
    kategori = "Produk Terlaris"
elif 500 <= penjualan <= 1000:
    kategori = "Produk Populer"
else:
    kategori = "Produk Biasa"

# Mencetak kategori produk
print(f"Kategori produk: {kategori}")
