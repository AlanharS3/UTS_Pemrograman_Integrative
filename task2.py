# Nama : Al Anhar Sufi
# NIM  : 211402045

import datetime

def hitung_hasil(number):
    hasil_kali = 1
    for i in range(1, number + 1):
        hasil_kali *= i
    return hasil_kali

def main():
    tanggal = datetime.datetime(2024, 3, 25).day

    hasil = hitung_hasil(tanggal)
    print("Tanggal tes hari ini adalah Senin, 25 Maret 2024")
    print("Maka hasil perkalian dari semua nilai dari 1 hingga", tanggal, "adalah:", hasil)

if __name__ == "__main__":
    main()
