import tkinter as tk

# Fungsi untuk menghasilkan prediksi
def hasil_prediksi():
    # Menampilkan hasil prediksi di label
    label_hasil.config(text="Prodi Pilihan: Teknologi Informasi")

# Membuat window utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x600")

# Menambahkan warna latar belakang
root.configure(bg="lightblue")

# Membuat label judul aplikasi
label_judul = tk.Label(root, text="Prediksi Prodi Pilihan", font=("Mv Boli", 16, "bold"), bg="lightblue")
label_judul.grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")

# Membuat Frame untuk bagian input nilai mata pelajaran
frame_input = tk.Frame(root, bg="lightblue")
frame_input.grid(row=1, column=0, columnspan=2, pady=10, padx=20, sticky="nsew")

# Membuat label dan entry untuk 10 nilai mata pelajaran dalam Frame
input_entries = []
for i in range(10):
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i+1}:", bg="lightblue")
    label.grid(row=i, column=0, padx=5, pady=3, sticky="w")
    entry = tk.Entry(frame_input)
    entry.grid(row=i, column=1, padx=10, pady=5)
    input_entries.append(entry)

# Membuat tombol untuk menghasilkan prediksi
button_prediksi = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
button_prediksi.grid(row=12, column=0, columnspan=2, pady=20, sticky="nsew")

# Membuat label untuk menampilkan hasil prediksi
label_hasil = tk.Label(root, text="Prodi Pilihan: ", font=("Mv Boli", 12), bg="lightblue")
label_hasil.grid(row=13, column=0, columnspan=2, sticky="nsew")

# Menjalankan aplikasi
root.mainloop()

