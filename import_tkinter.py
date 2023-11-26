import tkinter as tk
import sqlite3
def hasil_prediksi():
    # Mendapatkan nilai dari input pengguna
    nama = tk.Entry(top, entry_nama.get())  # Mendapatkan nama siswa dari entry_nama
    
    # Mendapatkan nilai dari 10 mata pelajaran (3 yang sudah ada + 10 tambahan)
    nilai_biologi = float(entry_biologi[1].get())
    nilai_fisika = float(entry_fisika.get())
    nilai_inggris = float(entry_inggris.get())
    nilai_mtk = float(entry_mtk.get())
    nilai_kimia = float(entry_kimia.get())
    nilai_sejarah = float(entry_sejarah.get())
    nilai_geografi = float(entry_geografi.get())
    nilai_seni = float(entry_seni.get())
    nilai_olahraga = float(entry_olahraga.get())
    nilai_tik = float(entry_tik.get())
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
    hasil_prodi.config(text=f"Prodi Pilihan: {hasil_prodi}")

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

top = tk.Tk()
top.title("Aplikasi Prediksi Prodi Pilihan") 
top.geometry("350x500")
# Code to add widgets will go here... 
judulProgram = tk.Label(top, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
judulProgram.grid(row=0, column=0, columnspan=2, pady=10)

textMasukan = tk.Label(top, text="Masukkan Nilai Mata Pelajaran: ", font=("Arial", 9))
textMasukan.grid(row=1, column=0, columnspan=1, padx=5, pady=10)

mata_pelajaran = ["Nama Siswa","Biologi","Fisika","Inggris"]
input_entries = []

for i, label_text in enumerate(mata_pelajaran) :
    MP = tk.Label(top, text=label_text)
    MP.grid(row=i + 2, column=0, pady=5)

    entry = tk.Entry(top)
    entry.grid(row=i+2, column=1, pady=5)
    input_entries.append(entry)



tombolHasil = tk.Button(top, text="Hasil Prediksi", command=hasil_prediksi)
tombolHasil.grid(row=14, column=0, columnspan=2, pady=2)

outputButton = tk.Label(top, text="")
outputButton.grid(row=15, column=0, columnspan=2, pady=10)


top.mainloop() 





