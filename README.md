# Praktikum-6

Nama : Tiara Hayatul Khoir

Kelas : TI.24.A.5

Nim : 312410474

Mata Kuliah : Bahasa pemrograman

## Program Sederhana Penggunaan Fungsi Sebagai Daftar Nilai Mahasiswa

### Penjelasan Program
Program ini adalah sistem manajemen data nilai mahasiswa yang memungkinkan pengguna untuk:
1. Menambah data mahasiswa berupa nama dan nilai.
2. Melihat daftar mahasiswa yang telah dimasukkan.
3. Menghapus data mahasiswa berdasarkan nama.
4. Mengubah nilai mahasiswa berdasarkan nama.

Tujuan dari program ini adalah untuk memberikan latihan dalam mengelola data menggunakan list dan dictionary, serta menerapkan logika pengolahan data menggunakan fungsi.

## Alur Penjelasan Kode Program

### 1. Inisialisasi
```python
mahasiswa = []: Membuat list kosong untuk menyimpan data mahasiswa dalam bentuk dictionary (contohnya: {"nama": "Budi", "nilai": 90}).
```

### 2. Fungsi 

**a)** `tambah(nama, nilai)`

**Input**: Nama dan nilai mahasiswa.

**Proses**: Menambahkan dictionary berisi nama dan nilai ke dalam `list mahasiswa`.

**Output**: Tidak ada, hanya menambah data ke list.

**b)** `tampilkan ()`

**Proses**:

Jika mahasiswa tidak kosong, program akan mencetak semua data dengan menggunakan enumerasi (nomor otomatis) pada setiap elemen.

Jika kosong, akan mencetak pesan "Belum ada data."

**Output**: Daftar data mahasiswa yang ada.

**c)** `hapus(nama)`

**Input**: Nama mahasiswa yang ingin dihapus.

**Proses**:

Menggunakan list comprehension untuk membuat list baru yang hanya berisi data mahasiswa selain nama yang dimasukkan. 
Data lama diganti dengan list baru tanpa nama yang dihapus.

**Output**: Tidak ada, hanya memodifikasi list `mahasiswa`.

**d)** `ubah(nama, nilai)`

**Input**: Nama mahasiswa dan nilai baru.

**Proses**:
Mengecek setiap elemen di list `mahasiswa`.
Jika ditemukan nama yang cocok, nilai pada dictionary tersebut diperbarui.

**Output**: Tidak ada, hanya memodifikasi list `mahasiswa`.

### 3. Menu Utama

**a)** `Tampilan Menu`

Meminta pengguna memilih salah satu opsi dari menu:
1. untuk menambah data mahasiswa.
2. untuk menampilkan semua data mahasiswa.
3. untuk menghapus data mahasiswa berdasarkan nama.
4. untuk mengubah nilai mahasiswa berdasarkan nama.
5. untuk keluar dari program.

**b)** `Proses Berdasarkan Pilihan`

`pilihan == "1":`
Meminta input nama dan nilai mahasiswa.
Memanggil fungsi tambah(nama, nilai) untuk menyimpan data.

`pilihan == "2":`
Memanggil fungsi tampilkan() untuk menampilkan semua data yang tersimpan.

`pilihan == "3":`
Meminta input nama mahasiswa yang akan dihapus.
Memanggil fungsi hapus(nama).

`pilihan == "4":`
Meminta input nama mahasiswa yang datanya akan diubah dan nilai baru.
Memanggil fungsi ubah(nama, nilai_baru).

`pilihan == "5":`
Program keluar dari loop dan berhenti.
Lainnya: Jika input tidak valid, program menampilkan pesan "Pilihan tidak valid."

### 4. Alur Program
1. Program akan terus berjalan dalam loop **while True** sampai pengguna memilih keluar `(pilihan == "5")`.
2. Pengguna memilih opsi dari menu.
3. Berdasarkan pilihan, program memanggil fungsi yang relevan.
4. Jika pengguna memilih keluar, program berhenti.

## Hasil Kode Program
![foto](https://github.com/tir890/foto/blob/cd3a05f6f1b321c8fbb6937c528a7b0c360aba00/Screenshot%202024-12-01%20154021.png)

