# Nama : Al Anhar Sufi
# NIM  : 211402045

import datetime

def main():
    # cek tahun sekarang
    tahun_now = datetime.datetime.now().year

    # cek hari pada tahun 
    jumlah_hari_tahun_now = 366 if tahun_kabisat(tahun_now) else 365

    # Input Pengguna
    bilangan = int(input("Masukkan bilangan bulat: "))

    # Hitung Hasil
    hasil = bilangan / jumlah_hari_tahun_now

    # Tampilkan hasil
    format_hasil = "{:.11f}".format(hasil)
    print("Hasil:", format_hasil)

#Menentukan tahun kabisat
def tahun_kabisat(tahun):
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)

if __name__ == "__main__":
    main()
