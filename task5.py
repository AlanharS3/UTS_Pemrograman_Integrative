# Nama : Al Anhar Sufi
# NIM  : 211402045

def baca_file(nama_file):
    with open(nama_file, 'r') as file:
        bilangan = [int(line.strip()) for line in file if line.strip().isdigit()]
    return bilangan

def format_jumlah(jumlah_bilangan):
    jumlah_terformat = "{:,}".format(jumlah_bilangan)
    return jumlah_terformat

def main():
    try:
        bilangan = baca_file("input.txt")
        jumlah_bilangan = sum(bilangan)
        jumlah_terformat = format_jumlah(jumlah_bilangan)
        print("Jumlah dari bilangan:", jumlah_terformat)
    except FileNotFoundError:
        print("File 'input.txt' tidak ditemukan.")
    except ValueError:
        print("Error: File berisi nilai non-bilangan bulat.")

if __name__ == "__main__":
    main()
