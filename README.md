# Praktikum-6

Nama : Tiara Hayatul Khoir

Kelas : TI.24.A.5

Nim : 312410474

Mata Kuliah : Bahasa pemrograman

## Program Sederhana Penggunaan Fungsi Sebagai Daftar Nilai Mahasiswa

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
