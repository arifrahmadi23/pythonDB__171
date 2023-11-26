import tkinter as tk
import sqlite3

def simpan_data_ke_sqlite(nilai1,nilai2, prodi_terpilih):
# Membuka atau membuat database SQLite
    conn = sqlite3.connect("Prediksi6.db")
    cursor = conn.cursor()
# Membuat tabel jika belum ada
    cursor.execute('''CREATE TABLE IF NOT EXISTS hasil_prediksi
    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nilai1 INTEGER, 
    nilai2 INTEGER,
    prodi_terpilih TEXT)''')
# Memasukkan data mata pelajaran ke dalam tabel
    cursor.execute("INSERT INTO hasil_prediksi (mata_pelajaran, nilai, prodi_terpilih) VALUES (?, ?, ?)",
    (nilai1, nilai2, prodi_terpilih))
# Melakukan commit dan menutup koneksi
    conn.commit()
    conn.close()

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

def outputButtonHasil ():
    outputButton.config(text="Hasil Prediksi : Teknologi Informasi")

tombolHasil = tk.Button(top, text="Hasil Prediksi", command=outputButtonHasil)
tombolHasil.grid(row=14, column=0, columnspan=2, pady=2)

outputButton = tk.Label(top, text="")
outputButton.grid(row=15, column=0, columnspan=2, pady=10)


top.mainloop() 





