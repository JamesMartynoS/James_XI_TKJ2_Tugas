#Nama           : James Martyno S
#Kelas          : XI TKJ 2
#Nomor Absen    : 15
#Soal : Buatlah sebuah fungsi yang menghitung bilangan Fibonacci ke-n.

def fibo(n):
    if n <= 0:
        return
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n -1) + fibo(n -2)
    
n = int(input("Masukkan nilai n untuk bilangan Fibonacci ke-n: "))

hasil = fibo(n)

if hasil != "Input tidak valid":
    print(f"bilangan fibonanci ke-{n} adalah {hasil}")
else:
    print(hasil)