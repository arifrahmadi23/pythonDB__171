# Import library yang diperlukan
import tkinter as tk  # Import modul tkinter untuk membuat GUI
import sqlite3  # Import modul sqlite3 untuk berinteraksi dengan database SQLite

# Fungsi yang dipanggil saat tombol "Submit Nilai" ditekan
def hasil_prediksi():
    # Mendapatkan nilai dari input pengguna
    nama = entry_nama.get()  # Mendapatkan nama siswa dari entry_nama
    
    # Mendapatkan nilai dari 10 mata pelajaran (3 yang sudah ada + 10 tambahan)
    nilai_biologi = float(entry_biologi.get())
    nilai_fisika = float(entry_fisika.get())
    # ... (nilai dari mata pelajaran lainnya)

    # Menentukan hasil prediksi berdasarkan nilai tertinggi
    nilai_tinggi = max(nilai_biologi, nilai_fisika, nilai_inggris, nilai_mtk, nilai_kimia,
                       nilai_sejarah, nilai_geografi, nilai_seni, nilai_olahraga,
                       nilai_tik)

    # Menentukan program studi berdasarkan nilai tertinggi dari mata pelajaran
    if nilai_tinggi == nilai_biologi:
        hasil_prodi = "Kedokteran"
    # ... (penentuan program studi berdasarkan kondisi lainnya)
    else:
        hasil_prodi = "Belum dapat diprediksi"

    # Menampilkan hasil prediksi pada GUI
    hasil.config(text=f"Prodi Pilihan: {hasil_prodi}")

    # Menyimpan data ke dalam database SQLite
    conn = sqlite3.connect('nilai_siswa.db')  # Membuka koneksi ke database
    cursor = conn.cursor()  # Membuat cursor untuk eksekusi query SQL

    # Membuat tabel jika belum ada
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nama_siswa TEXT,
                        biologi REAL,
                        fisika REAL,
                        # ... (kolom untuk nilai mata pelajaran lainnya)
                        prediksi_fakultas TEXT
                    )''')

    # Menyimpan data nilai siswa ke dalam tabel
    cursor.execute('''INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, mtk,
                    # ... (kolom untuk nilai mata pelajaran lainnya)
                    prediksi_fakultas)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (nama, nilai_biologi, nilai_fisika, nilai_inggris, nilai_mtk, nilai_kimia,
                    nilai_sejarah, nilai_geografi, nilai_seni, nilai_olahraga,
                    nilai_tik, hasil_prodi))
    conn.commit()  # Melakukan commit perubahan ke dalam database
    conn.close()  # Menutup koneksi ke database setelah selesai

# Membuat jendela aplikasi menggunakan Tkinter
root = tk.Tk()  # Membuat instance dari Tkinter
root.title("Aplikasi Prediksi Prodi Pilihan")  # Memberikan judul pada jendela
root.geometry("500x600")  # Mengatur ukuran jendela

# Membuat elemen-elemen GUI (label, entry, button, dan output hasil)
# ... (pembuatan label, entry, button, dan hasil prediksi)

root.mainloop()  # Memulai loop utama untuk menampilkan GUI