mahasiswa = []

def tambah(nama, nilai): mahasiswa.append({"nama": nama, "nilai": nilai})
def tampilkan(): 
    if mahasiswa: 
        [print(f"{i+1}. Nama: {m['nama']}, Nilai: {m['nilai']}") for i, m in enumerate(mahasiswa)]
    else: print("Belum ada data.")
def hapus(nama): 
    global mahasiswa
    mahasiswa = [m for m in mahasiswa if m["nama"] != nama]
def ubah(nama, nilai): 
    for m in mahasiswa: 
        if m["nama"] == nama: m["nilai"] = nilai

while True:
    menu = input("\n1.Tambah 2.Tampil 3.Hapus 4.Ubah 5.Keluar: ")
    if menu == "1": tambah(input("Nama: "), float(input("Nilai: ")))
    elif menu == "2": tampilkan()
    elif menu == "3": hapus(input("Nama yang dihapus: "))
    elif menu == "4": ubah(input("Nama yang diubah: "), float(input("Nilai baru: ")))
    elif menu == "5": break
    else: print("Pilihan tidak valid.")
