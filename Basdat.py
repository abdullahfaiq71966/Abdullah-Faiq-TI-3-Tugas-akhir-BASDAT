import sqlite3

# Fungsi untuk membuka koneksi ke database
def buka_koneksi():
    return sqlite3.connect(r'C:\Users\samsung-pc\Pictures\Ngapain kuliah !\CODING_KULIAH\Python\.venv\Basdat klinik.db')

# 1. Fungsi Pendaftaran Pasien
def tambah_pasien():
    print("\n=== PENDAFTARAN PASIEN BARU ===")
    nama = input("Masukkan Nama Pasien: ")
    tgl_lahir = input("Masukkan Tanggal Lahir (YYYY-MM-DD): ")
    kelamin = input("Masukkan Kelamin (Pria/Wanita): ")
    no_telp = input("Masukkan No Telp: ")
    usia = int(input("Masukkan Usia (Angka): "))

    conn = buka_koneksi()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Pasien (Nama_pasien, Tanggal_Lahir, Kelamin, No_telp, Usia)
        VALUES (?, ?, ?, ?, ?)
    ''', (nama, tgl_lahir, kelamin, no_telp, usia))
    conn.commit()
    conn.close()
    print("✅ Berhasil: Data pasien tersimpan!")

# 2. Fungsi Input Bio Dokter
def tambah_dokter():
    print("\n=== INPUT DATA DOKTER ===")
    nama = input("Masukkan Nama Dokter: ")
    spesialisasi = input("Masukkan Spesialisasi: ")
    no_telp = input("Masukkan No Telp: ")

    conn = buka_koneksi()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Dokter (nama, Spesialisasi, no_telp)
        VALUES (?, ?, ?)
    ''', (nama, spesialisasi, no_telp))
    conn.commit()
    conn.close()
    print("✅ Berhasil: Data dokter tersimpan!")

# 3. Fungsi Input Data Obat
def tambah_obat():
    print("\n=== INPUT DATA OBAT ===")
    nama_obat = input("Masukkan Nama Obat: ")
    stok = int(input("Masukkan Jumlah Stok: "))
    keterangan = input("Masukkan Keterangan (Dosis/Aturan pakai): ")

    conn = buka_koneksi()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Obat (nama_obat, stok, keterangan)
        VALUES (?, ?, ?)
    ''', (nama_obat, stok, keterangan))
    conn.commit()
    conn.close()
    print("✅ Berhasil: Data obat tersimpan!")

# 4. Fungsi Pembuatan Janji Temu
def buat_janji():
    print("\n=== BUAT JANJI TEMU ===")
    # Menampilkan daftar pasien singkat untuk panduan
    conn = buka_koneksi()
    cursor = conn.cursor()
    
    print("--- Panduan ID Pasien ---")
    cursor.execute("SELECT id, Nama_pasien FROM Pasien")
    for p in cursor.fetchall():
        print(f"ID: {p[0]} | Nama: {p[1]}")
        
    print("\n--- Panduan ID Dokter ---")
    cursor.execute("SELECT id_dokter, nama, Spesialisasi FROM Dokter")
    for d in cursor.fetchall():
        print(f"ID: {d[0]} | Nama: {d[1]} ({d[2]})")
        
    print("-" * 25)
    id_pasien = int(input("Masukkan ID Pasien: "))
    id_dokter = int(input("Masukkan ID Dokter: "))
    tanggal = input("Masukkan Tanggal & Waktu (YYYY-MM-DD HH:MM): ")

    cursor.execute('''
        INSERT INTO Janji_Temu (id_pasien, id_dokter, Tanggal)
        VALUES (?, ?, ?)
    ''', (id_pasien, id_dokter, tanggal))
    conn.commit()
    conn.close()
    print("✅ Berhasil: Janji temu telah dijadwalkan!")

# 5. Fungsi Memperlihatkan Jadwal Janji Temu (Menggunakan JOIN)
def lihat_jadwal():
    print("\n=== JADWAL JANJI TEMU KLINIK ===")
    conn = buka_koneksi()
    cursor = conn.cursor()
    
    # Query JOIN untuk menggabungkan nama pasien dan nama dokter
    query = '''
        SELECT Janji_Temu.id_janji, Pasien.Nama_pasien, Dokter.nama, Janji_Temu.Tanggal
        FROM Janji_Temu
        JOIN Pasien ON Janji_Temu.id_pasien = Pasien.id
        JOIN Dokter ON Janji_Temu.id_dokter = Dokter.id_dokter
        ORDER BY Janji_Temu.Tanggal ASC
    '''
    cursor.execute(query)
    jadwal = cursor.fetchall()
    
    if len(jadwal) == 0:
        print("Belum ada jadwal janji temu saat ini.")
    else:
        # Menampilkan data dalam format tabel yang rapi
        print(f"{'ID Janji':<10} | {'Nama Pasien':<20} | {'Nama Dokter':<20} | {'Waktu'}")
        print("-" * 75)
        for baris in jadwal:
            print(f"{baris[0]:<10} | {baris[1]:<20} | {baris[2]:<20} | {baris[3]}")
            
    conn.close()

# Main Menu (Looping agar program tidak langsung keluar)
def menu_utama():
    while True:
        print("\n" + "="*35)
        print("SISTEM MANAJEMEN KLINIK")
        print("="*35)
        print("1. Pendaftaran Pasien Baru")
        print("2. Input Bio Dokter")
        print("3. Input Data Obat")
        print("4. Buat Janji Temu")
        print("5. Lihat Jadwal Janji Temu")
        print("0. Keluar")
        
        pilihan = input("Pilih menu (0-5): ")
        
        if pilihan == '1':
            tambah_pasien()
        elif pilihan == '2':
            tambah_dokter()
        elif pilihan == '3':
            tambah_obat()
        elif pilihan == '4':
            buat_janji()
        elif pilihan == '5':
            lihat_jadwal()
        elif pilihan == '0':
            print("Terima kasih telah menggunakan sistem klinik!")
            break
        else:
            print("❌ Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program
if __name__ == "__main__":
    menu_utama()