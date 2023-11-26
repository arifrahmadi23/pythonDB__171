import tkinter as tk
import sqlite3


def hasil_prediksi():
    # Mendapatkan nilai dari input
    nama = entry_nama.get()
    nilai_biologi = float(entry_biologi.get())
    nilai_fisika = float(entry_fisika.get())
    nilai_inggris = float(entry_inggris.get())
    nilai_sosiologi = float(entry_sosiologi.get())
    nilai_matematika = float(entry_matematika.get())
    nilai_kimia = float (entry_kimia.get())
    nilai_sejarah = float(entry_sejarah.get())
    nilai_tik = float(entry_tik.get())
    nilai_ppkn = float(entry_ppkn.get())
    nilai_geografi = float(entry_geografi.get())


    # Menentukan hasil nilai prediksi berdasarkan yang tertinggi
    # Membandingkan nilai dari 10 mata pelajaran
    nilai_tinggi = max(nilai_biologi, nilai_fisika, nilai_inggris, nilai_sosiologi, nilai_matematika, nilai_kimia, 
                       nilai_sejarah, nilai_tik, nilai_ppkn, nilai_geografi)
    

    if nilai_tinggi == nilai_biologi:
        hasil_prodi = "Kedokteran"
    elif nilai_tinggi == nilai_fisika:
        hasil_prodi = "Teknik"
    elif nilai_tinggi == nilai_inggris:
        hasil_prodi = "Bahasa"
    elif nilai_tinggi == nilai_sosiologi:
        hasil_prodi = "Pisikologi"
    elif nilai_tinggi == nilai_matematika:
        hasil_prodi = "Pendidikan"
    elif nilai_tinggi == nilai_sejarah:
        hasil_prodi = "Ilmu Sejarah"
    elif nilai_tinggi == nilai_tik:
        hasil_prodi = "Teknik Informatika"
    elif nilai_tinggi == nilai_ppkn:
        hasil_prodi = "Hukum"
    elif nilai_tinggi == nilai_geografi:
        hasil_prodi = "Geografi"
    else:
        hasil_prodi = "Belum dapat diprediksi"

    # Menampilkan hasil prediksi
    hasil.config(text=f"Prodi Pilihan: {hasil_prodi}")

    # Menyimpan data ke SQLite
    conn = sqlite3.connect('deni2.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nama_siswa TEXT,
                        biologi REAL,
                        fisika REAL,
                        inggris REAL,
                        sosiologi REAL,
                        matematika REAL,
                        sejarah REAL,
                        tik REAL,
                        ppkn REAL,
                        geografi REAL,
                        prediksi_fakultas TEXT
                    )''')
    cursor.execute('''INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, sosiologi, matematika, sejarah, tik, ppkn, prediksi_fakultas)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (nama, nilai_biologi, nilai_fisika, nilai_inggris,nilai_sosiologi, nilai_matematika,
                                                               nilai_sejarah, nilai_tik, nilai_ppkn, nilai_geografi, hasil_prodi))
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

label_sosiologi = tk.Label(root, text="Nilai Sosiologi: ")
label_sosiologi.pack()
entry_sosiologi = tk.Entry(root)
entry_sosiologi.pack()

label_matematika = tk.Label(root, text="Nilai Matekamtika: ")
label_matematika.pack()
entry_matematika = tk.Entry(root)
entry_matematika.pack()

label_kimia = tk.Label(root, text="Nilai Kimia: ")
label_kimia.pack()
entry_kimia = tk.Entry(root)
entry_kimia.pack()

label_sejarah = tk.Label(root, text="Nilai Sejarah: ")
label_sejarah.pack()
entry_sejarah = tk.Entry(root)
entry_sejarah.pack()

label_tik = tk.Label(root, text="Nilai TIK: ")
label_tik.pack()
entry_tik = tk.Entry(root)
entry_tik.pack()

label_ppkn = tk.Label(root, text="Nilai PPKN: ")
label_ppkn.pack()
entry_ppkn = tk.Entry(root)
entry_ppkn.pack()

label_geografi = tk.Label(root, text="Nilai Geografi: ")
label_geografi.pack()
entry_geografi = tk.Entry(root)
entry_geografi.pack()

# Button Submit Nilai
button_submit = tk.Button(root, text="Submit Nilai", command=hasil_prediksi)
button_submit.pack(pady=10)

# Label luaran hasil prediksi
hasil = tk.Label(root, text="Prodi Pilihan: ", font=("Arial", 12))
hasil.pack()

root.mainloop()