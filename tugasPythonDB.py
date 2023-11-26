import tkinter as tk
import sqlite3

def hasil_prediksi():
    # Ambil nilai dari entry
    nama_siswa = input_entries[0].get()
    biologi = int(input_entries[1].get())
    fisika = int(input_entries[2].get())
    kimia = int(input_entries[3].get())
    matematika = int(input_entries[4].get())
    inggris = int(input_entries[5].get())
    bindonesia = int(input_entries[6].get())
    geografi = int(input_entries[7].get())
    ekonomi = int(input_entries[8].get())
    sosiologi = int(input_entries[9].get())
    pkn = int(input_entries[10].get())
    # Koneksikan ke database
    connection = sqlite3.connect("nilai_siswa9.db")
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nama_siswa TEXT,
                        biologi INTEGER,
                        fisika INTEGER,
                        kimia INTEGER,
                        matematika INTEGER,
                        inggris INTEGER,
                        bindonesia INTEGER,
                        geografi INTEGER,
                        ekonomi INTEGER,
                        sosiologi INTEGER,
                        pkn INTEGER,
                        prediksi_fakultas TEXT)''')

    # Masukkan data ke database
    cursor.execute("INSERT INTO nilai_siswa (nama_siswa, biologi, fisika,kimia, matematika, inggris, bindonesia, geografi, ekonomi, sosiologi, pkn, prediksi_fakultas) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (nama_siswa, biologi, fisika, kimia, matematika, inggris, bindonesia, geografi, ekonomi, sosiologi, pkn, ""))
    
    nilai_tertinggi = max(biologi, fisika, kimia, matematika, inggris, bindonesia, geografi, ekonomi, sosiologi, pkn,)
    # Tutup koneksi ke database
    connection.commit()
    connection.close()
    
    # Hitung hasil prediksi
    if nilai_tertinggi == biologi:
        prediksi_fakultas = "Kedokteran"
    elif nilai_tertinggi == fisika:
        prediksi_fakultas = "Teknik"
    elif nilai_tertinggi == kimia:
        prediksi_fakultas = "Teknik"
    elif nilai_tertinggi == matematika:
        prediksi_fakultas = "Matematika dan Ilmu Pengetahuan Alam"
    elif nilai_tertinggi == inggris:
        prediksi_fakultas = "Ilmu Sosial dan Humaniora"
    elif nilai_tertinggi == bindonesia:
        prediksi_fakultas = "Ilmu Sosial dan Humaniora"
    elif nilai_tertinggi == geografi:
        prediksi_fakultas = "Ilmu Sosial dan Humaniora"
    elif nilai_tertinggi == ekonomi:
        prediksi_fakultas = "Ekonomi"
    elif nilai_tertinggi == sosiologi:
        prediksi_fakultas = "Ilmu Sosial dan Humaniora"
    else:
        prediksi_fakultas = "Kreatif"

    # Tampilkan hasil prediksi
    outputButton.config(text="Hasil prediksi: " + prediksi_fakultas)


top = tk.Tk()
top.title("Aplikasi Prediksi Prodi Pilihan")
top.geometry("350x500")

judulProgram = tk.Label(top, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
judulProgram.grid(row=0, column=0, columnspan=2, pady=10)

textMasukan = tk.Label(top, text="Masukkan Nilai Mata Pelajaran: ", font=("Arial", 9))
textMasukan.grid(row=1, column=0, columnspan=1, padx=5, pady=10)

mata_pelajaran = ["Nama Siswa", "Biologi", "Fisika","Kimia", "Matematika", "Bahasa Inggris", "Bahasa Indonesia", "Geografi", "Ekonomi", "Sosiologi", "PKN"]
input_entries = []

for i, label_text in enumerate(mata_pelajaran):
    MP = tk.Label(top, text=label_text)
    MP.grid(row=i + 2, column=0, pady=5)

    entry = tk.Entry(top)
    entry.grid(row=i + 2, column=1, pady=5)
    input_entries.append(entry)

tombolHasil = tk.Button(top, text="Hasil Prediksi", command=hasil_prediksi)
tombolHasil.grid(row=14, column=0, columnspan=2, pady=2)

outputButton = tk.Label(top, text="")
outputButton.grid(row=15, column=0, columnspan=2, pady=10)

top.mainloop()
