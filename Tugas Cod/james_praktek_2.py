#Nama: James Martyno S
#Kelas: XI TKJ 2
#Nomor Absen: 15
#Soal:Buat program yang menghitung berapa minggu untuk dibutuhkan agar pelari itu dapat berlari lebih dari 10 km.

jarak_awal = 5
jarak_peningkatan = 10
minggu = 0

while jarak_awal < jarak_peningkatan:
    jarak_awal = jarak_awal + 0.10 * jarak_awal
    minggu += 1
    print(f'jarak {jarak_awal} kilometar pada setiap minggu {minggu}')

print(f'Dibutuhkan {minggu} minggu untuk pelari mencapai lebih dari 10 km')