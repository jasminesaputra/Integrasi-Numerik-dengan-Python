# Integrasi Numerik dengan Python  
## Metode Trapesium dan Simpson 1/3

Repository ini berisi implementasi **integrasi numerik** menggunakan bahasa pemrograman **Python**, dengan membandingkan **Metode Trapesium** dan **Metode Simpson 1/3**.  
Proyek ini dibuat sebagai bagian dari **Tugas Metode Numerik (Bagian 2)**.

---

## 📌 Informasi Mahasiswa
- **Nama:** Jasmine Saputra  
- **NIM:** 21120123140145  
- **Kelas:** Metode Numerik A  
- **Program Studi:** Teknik Komputer  

---

## 📖 Deskripsi Proyek
Dalam perhitungan teknik dan sains, integral sering digunakan untuk menentukan besaran fisik seperti luas, energi, dan usaha. Namun, tidak semua integral dapat dihitung secara analitik dengan mudah. Oleh karena itu, digunakan metode numerik sebagai pendekatan.

Pada proyek ini, dihitung nilai integral dari fungsi:

\[
F(x) = 10 + 2x^2
\]

pada interval \([0, 3]\), yang merepresentasikan **usaha (work)** dari gaya terhadap perpindahan.  
Hasil integrasi numerik dibandingkan dengan nilai integral analitik sebagai referensi.

---

## 🧮 Metode yang Digunakan
1. **Metode Trapesium (Composite Trapezoidal Rule)**  
   Menghampiri kurva dengan trapesium pada setiap sub-interval.

2. **Metode Simpson 1/3 (Composite Simpson’s Rule)**  
   Menggunakan pendekatan polinom kuadratik dan membutuhkan jumlah partisi genap.

---

## 🧪 Fitur Program
- Menghitung integral numerik dengan Metode Trapesium
- Menghitung integral numerik dengan Metode Simpson 1/3
- Membandingkan hasil dengan nilai analitik
- Menampilkan nilai error dari masing-masing metode
- Output berbentuk tabel di terminal

---

## 💻 Cara Menjalankan Program

### 1️⃣ Clone repository
```bash
git clone https://github.com/username/integrasi-numerik-python.git
cd integrasi-numerik-python
