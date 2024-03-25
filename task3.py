# Nama : Al Anhar Sufi
# NIM  : 211402045

import datetime

def cetak_tanggal_nanti(jumlah_hari):
    # cek tanggal hari ini
    hari_ini = datetime.datetime.now()

    # Hitung tanggal mendatang
    tanggal_mendatang = hari_ini + datetime.timedelta(days=jumlah_hari)

    # Format tanggal mendatang
    tanggal_terformat = tanggal_mendatang.strftime("%A, on %d %B %Y")

    # Cetak tanggal
    print("Tanggal", jumlah_hari, "hari dari sekarang adalah:", tanggal_terformat)

def main():
    try:
        jumlah_hari = int(input("Masukkan jumlah hari dari sekarang: "))
        if jumlah_hari < 0:
            raise ValueError("Mohon masukkan bilangan bulat positif.")
        
        cetak_tanggal_nanti(jumlah_hari)

    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()

