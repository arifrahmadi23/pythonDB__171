import tkinter as tk
import sqlite3

def hasil_prediksi():
    # Mendapatkan nilai dari input
    nama = entry_nama.get()
    nilai_biologi = float(entry_biologi.get())
    nilai_fisika = float(entry_fisika.get())
    nilai_inggris = float(entry_inggris.get())

    # Menentukan hasil prediksi berdasarkan nilai tertinggi
    if nilai_biologi > nilai_fisika and nilai_biologi > nilai_inggris:
        hasil_prodi = "Kedokteran"
    elif nilai_fisika > nilai_biologi and nilai_fisika > nilai_inggris:
        hasil_prodi = "Teknik"
    elif nilai_inggris > nilai_biologi and nilai_inggris > nilai_fisika:
        hasil_prodi = "Bahasa"
    else:
        hasil_prodi = "Belum dapat diprediksi"

    # Menampilkan hasil prediksi
    hasil.config(text=f"Prodi Pilihan: {hasil_prodi}")

    # Menyimpan data ke SQLite
    conn = sqlite3.connect('nilai_siswa.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nama_siswa TEXT,
                        biologi REAL,
                        fisika REAL,
                        inggris REAL,
                        prediksi_fakultas TEXT
                    )''')
    cursor.execute('''INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
                    VALUES (?, ?, ?, ?, ?)''', (nama, nilai_biologi, nilai_fisika, nilai_inggris, hasil_prodi))
    conn.commit()
    conn.close()

# Membuat jendela Tkinter
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x400")  # Mengatur ukuran jendela

# Label judul
label_judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))
label_judul.pack(pady=10)

# Input nilai mata pelajaran
label_nama = tk.Label(root, text="Nama Siswa: ")
label_nama.pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

label_biologi = tk.Label(root, text="Nilai Biologi: ")
label_biologi.pack()
entry_biologi = tk.Entry(root)
entry_biologi.pack()

label_fisika = tk.Label(root, text="Nilai Fisika: ")
label_fisika.pack()
entry_fisika = tk.Entry(root)
entry_fisika.pack()

label_inggris = tk.Label(root, text="Nilai Inggris: ")
label_inggris.pack()
entry_inggris = tk.Entry(root)
entry_inggris.pack()

# Button Submit Nilai
button_submit = tk.Button(root, text="Submit Nilai", command=hasil_prediksi)
button_submit.pack(pady=10)

# Label luaran hasil prediksi
hasil = tk.Label(root, text="Prodi Pilihan: ", font=("Arial", 12))
hasil.pack()

root.mainloop()