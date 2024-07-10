def main():
    mahasiswa = []

    while True:
        nim = input("masukkan NIM: ")
        nama = input("masukkan Nama: ")
        mahasiswa.append((nim, nama))
        tambah_lagi = input("ingin menambah lagi? (ya/tidak): ").lower()
        if tambah_lagi != 'ya':
            break

    print("\nData Mahasiswa:")
    for nim, nama in mahasiswa:
        print(f"NIM: {nim}, nama: {nama}")

if __name__ == "__main__":
    main()
