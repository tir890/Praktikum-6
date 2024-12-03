# Praktikum-6

Nama : Tiara Hayatul Khoir

Kelas : TI.24.A.5

Nim : 312410474

Mata Kuliah : Bahasa pemrograman

## Program Sederhana Penggunaan Fungsi Sebagai Daftar Nilai Mahasiswa

Program ini adalah sistem manajemen data nilai mahasiswa yang memungkinkan pengguna untuk:
1. Menambah data mahasiswa berupa nama dan nilai.
2. Melihat daftar mahasiswa yang telah dimasukkan.
3. Menghapus data mahasiswa berdasarkan nama.
4. Mengubah nilai mahasiswa berdasarkan nama.

Tujuan dari program ini adalah untuk memberikan latihan dalam mengelola data menggunakan list dan dictionary, serta menerapkan logika pengolahan data menggunakan fungsi.

## Alur Penjelasan Kode Program

1. **Pendefinisian Data**:
Program menggunakan sebuah dictionary `data_mahasiswa` untuk menyimpan data mahasiswa, dengan struktur:
     ```python
     data_mahasiswa = {
         "nama": {"nim": "312410474", "tugas": 77.0, "uts": 88.0, "uas": 99.0}
     }
     ```
     Setiap mahasiswa disimpan berdasarkan **nama** sebagai kunci (key), dan nilai-nilai lainnya (`nim`, `tugas`, `uts`, `uas`) sebagai dictionary.

2. **Fungsi `tampilkan_data()`**:
   **Tujuan**: Menampilkan data mahasiswa dalam bentuk tabel.
   
   •	Jika data tersedia, fungsi ini mencetak daftar mahasiswa beserta nilai akhir (perhitungan: `(tugas * 0.3) + (uts * 0.35) + (uas * 0.35)`).
   
   •	Jika tidak ada data, akan menampilkan pesan **"TIDAK ADA DATA"**.

3. **Fungsi `tambah_data()`**:
   **Tujuan**: Menambahkan data mahasiswa baru.
   
   Input berupa:
   
   •	**Nama**: Sebagai kunci utama.
   
   •	**NIM, Tugas, UTS, UAS**: Data lainnya.
   
   Data disimpan ke dalam `data_mahasiswa` setelah diinput.

4. **Fungsi `hapus_data()`**:
   **Tujuan**: Menghapus data mahasiswa berdasarkan nama.
   
   •	Jika nama ditemukan, data dihapus menggunakan `pop()`.
   
   •	Jika tidak ditemukan, mencetak pesan bahwa data tidak ada.

5. **Fungsi `ubah_data()`**:
   **Tujuan**: Mengubah data mahasiswa yang sudah ada.
   Input berupa:

   •	Nama mahasiswa yang ingin diubah.
   
   •	Nilai baru untuk `tugas`, `uts`, dan `uas`.
   
   Program memodifikasi nilai langsung dalam dictionary menggunakan `.update()`.

6. **Menu Utama**:
   Menampilkan menu pilihan untuk pengguna:
   •	`(L)ihat`: Memanggil `tampilkan_data()` untuk melihat data.

   •	`(T)ambah`: Memanggil `tambah_data()` untuk menambahkan data.
   
   •	`(H)apus`: Memanggil `hapus_data()` untuk menghapus data.
   
   •	`(U)bah`: Memanggil `ubah_data()` untuk mengubah data.
   
   •	`(K)eluar`: Keluar dari program.
   
   Pengguna memasukkan pilihan, dan program menjalankan fungsi yang sesuai.

7. **Pengulangan Program**:
   
   •	 Program berjalan terus dalam loop `while` sampai pengguna memilih `(K)eluar`.
   
   •	Jika pilihan menu tidak valid, program mencetak pesan **"Pilihan tidak valid!"**.
---

### **Fungsi Program**

#### **1. Input Data Mahasiswa**
Menambahkan data baru dengan nama sebagai kunci utama.
  Data mahasiswa terdiri dari:

  •	NIM: Nomor Induk Mahasiswa.

  •	Nilai Tugas, UTS, dan UAS.
  
  •	Nilai akhir dihitung otomatis berdasarkan bobot tertentu.

#### **2. Menampilkan Data Mahasiswa**
•	Data ditampilkan dalam format tabel dengan informasi berikut:
•	Nomor urut, Nama, NIM, Nilai Tugas, UTS, UAS, dan Nilai Akhir.
•	Jika tidak ada data, program menampilkan pesan bahwa data kosong.

#### **3. Mengubah Data Mahasiswa**
Memperbarui nilai tugas, UTS, dan UAS berdasarkan nama mahasiswa. Nilai akhir diperbarui otomatis setelah data diubah.

#### **4. Menghapus Data Mahasiswa**
Menghapus data mahasiswa dari daftar berdasarkan nama. Jika nama tidak ditemukan, menampilkan pesan kesalahan.

#### **5. Keluar dari Program**
Menutup program ketika pengguna memilih menu `(K)eluar`.

---

### **Ilustrasi Alur Eksekusi**

1. Program menampilkan menu utama:
   ```
   [(L)ihat, (T)ambah, (U)bah, (H)apus, (K)eluar] Pilih menu:
   ```
2. Pengguna memilih opsi:
   •	Jika **L**: Menampilkan daftar mahasiswa.
   
   •	Jika **T**: Memasukkan data mahasiswa baru.
   
   •	Jika **U**: Mengubah data mahasiswa tertentu.
   
   •	Jika **H**: Menghapus data mahasiswa berdasarkan nama.
   
   •	Jika **K**: Keluar dari program.
4. Program terus berjalan dalam loop sampai pengguna memilih untuk keluar.
5. Pesan dan output tampil sesuai tindakan pengguna.

## Hasil Kode Program
![Praktikum-6](https://github.com/tir890/Praktikum-6/blob/038bd28f0169a090070056026cadae10e98e4d68/Screenshot%202024-12-03%20104427.png)

## Gambar Flowchart
![Praktikum-6](https://github.com/tir890/Praktikum-6/blob/32bb2f2beb6ee37c3e4bb893d7abd05d9a663570/Blank%20diagram%20(12).png)
