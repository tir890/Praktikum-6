data_mahasiswa = {}

def tampilkan_data():
    print("\nDaftar Nilai")
    print("="*63)
    print("| NO |       NAMA      |    NIM    | TUGAS | UTS | UAS |  AKHIR  |")
    print("="*63)
    if data_mahasiswa:
        for no, (nama, data) in enumerate(data_mahasiswa.items(), start=1):
            akhir = (data['tugas'] * 0.3) + (data['uts'] * 0.35) + (data['uas'] * 0.35)
            print(f"| {no:<2} | {nama:<15} | {data['nim']:<8} | {data['tugas']:<5.0f} | {data['uts']:<3.0f} | {data['uas']:<3.0f} | {akhir:<7.2f} |")
    else:
        print("|                       TIDAK ADA DATA                      |")
    print("="*63)

def tambah_data():
    nama, nim = input("Nama: ").strip(), input("NIM: ").strip()
    try:
        tugas, uts, uas = (float(input(f"Nilai {k}: ")) for k in ["Tugas", "UTS", "UAS"])
        data_mahasiswa[nama] = {'nim': nim, 'tugas': tugas, 'uts': uts, 'uas': uas}
        print("Data berhasil ditambahkan!")
    except ValueError:
        print("Nilai harus berupa angka!")

def hapus_data():
    nama = input("Nama yang akan dihapus: ").strip()
    print("Data berhasil dihapus!" if data_mahasiswa.pop(nama, None) else "Data tidak ditemukan!")

def ubah_data():
    nama = input("Nama yang akan diubah: ").strip()
    if nama in data_mahasiswa:
        try:
            tugas, uts, uas = (float(input(f"Nilai baru {k}: ")) for k in ["Tugas", "UTS", "UAS"])
            data_mahasiswa[nama].update({'tugas': tugas, 'uts': uts, 'uas': uas})
            print("Data berhasil diubah!")
        except ValueError:
            print("Nilai harus berupa angka!")
    else:
        print("Data tidak ditemukan!")

while True:
    menu = input("\n[(L)ihat, (T)ambah, (U)bah, (H)apus, (K)eluar] Pilih menu: ").lower()
    if menu == 'l': tampilkan_data()
    elif menu == 't': tambah_data()
    elif menu == 'h': hapus_data()
    elif menu == 'u': ubah_data()
    elif menu == 'k': print("Terima kasih!"); break
    else: print("Pilihan tidak valid!")
