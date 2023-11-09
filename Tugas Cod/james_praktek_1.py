#Nama           : James Martyno S
#Kelas          : XI TKJ 2
#Nomor Absen    : 15
#Soal           : membutuhkan waktu berapa bulan agar penaikkan ayam dari jumlah pertama 100 jadi 200 ayam dengan penaikkan 5% bulan

jumlah_ayam_pertama = 100
target_ayam_diakhir = 200
bulan = 0

while jumlah_ayam_pertama <= target_ayam_diakhir:
    bulan += 1
    pertambahan_ayam = jumlah_ayam_pertama * 0.05
    jumlah_ayam_pertama += pertambahan_ayam
    print(f'pertumbuhan ayam {jumlah_ayam_pertama} pada bulan ke {bulan}')

print(f'Dibutuhkan {bulan} bulan agar jumlah ayam melebihi {target_ayam_diakhir} ekor.')