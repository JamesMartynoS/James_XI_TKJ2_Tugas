#Nama           : James Martyno S
#Kelas          : XI TKJ 2
#Nomor Absen    : 15
#Soal           : Buatlah progam yang menghitung berapa tahun yang dibutuhkan agar investasi melebihi 20.000 dollar

investasi_awal_tahun = 10000
target_investasi = 20000
tahun = 0

while investasi_awal_tahun < target_investasi:
    investasi_awal_tahun = investasi_awal_tahun + 0.06 * investasi_awal_tahun
    tahun += 1
    print(f'Nilai investasi {investasi_awal_tahun} pada tahun ke {tahun}')

print(f'Dibutuhkan {tahun} tahun agar nilai investasi mencapai 20.000 dollar')