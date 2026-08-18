    DROP TABLE IF EXISTS Rekam_medis;
    DROP TABLE IF EXISTS Janji_Temu;
    DROP TABLE IF EXISTS Obat;
    DROP TABLE IF EXISTS Dokter;
    DROP TABLE IF EXISTS Pasien;

    CREATE TABLE Pasien (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        Nama_pasien TEXT(50) DEFAULT NULL,
        Tanggal_Lahir DATE,
        Kelamin TEXT DEFAULT 'Non binary', 
        No_telp TEXT(15), 
        Usia INTEGER
    );

    CREATE TABLE Dokter (
        id_dokter INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nama TEXT,
        Spesialisasi TEXT,
        no_telp TEXT(15)
    );

    CREATE TABLE Obat (
        id_obat INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nama_obat TEXT,
        stok INTEGER NOT NULL DEFAULT 0,
        keterangan TEXT NOT NULL DEFAULT '-'
    );

    CREATE TABLE Janji_Temu (
        id_janji INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        id_pasien INTEGER NOT NULL,
        id_dokter INTEGER NOT NULL,
        Tanggal DATETIME,
        FOREIGN KEY(id_pasien) REFERENCES Pasien(id),
        FOREIGN KEY(id_dokter) REFERENCES Dokter(id_dokter)
    );

    CREATE TABLE Rekam_medis (
        id_rekam INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        id_pasien INTEGER NOT NULL,
        id_dokter INTEGER NOT NULL,
        id_janji INTEGER NOT NULL,
        id_obat INTEGER,
        FOREIGN KEY(id_pasien) REFERENCES Pasien(id),
        FOREIGN KEY(id_dokter) REFERENCES Dokter(id_dokter),
        FOREIGN KEY(id_janji) REFERENCES Janji_Temu(id_janji),
        FOREIGN KEY(id_obat) REFERENCES Obat(id_obat)
    );

INSERT INTO Pasien (Nama_pasien, Tanggal_Lahir, Kelamin, No_telp, Usia)
VALUES 
    ('Andi', '1990-05-14', 'Pria', '081234567890', 36),
	('Rika', '2006-02-14', 'Wanita', '08197952055', 20),
	('Xeon', '2012-05-19', 'Pria', '081234567890', 14),
	('Miko', '2012-02-10', 'Pria', '081237777890', 14),
	('Arona', '2010-05-14', 'Wanita', '081234566666', 16),
	('Astolfo', '2007-05-14', 'Pria', '081234567890', 19),
	('Haruka', '2010-01-08', 'Pria', '081234567890', 16),
	('Hiura', '2015-05-14', 'Pria', '081234567890', 11),
	('Ju Fufu', '2010-01-10', 'Wanita', '081234566554', 16),
    ('Siti', '2001-11-20', 'Wanita', '089876543210', 25);
	
INSERT INTO Dokter (nama,Spesialisasi,no_telp)
VALUES	
	('Ahmad Maspion','Jantung','081234567890'),
	('Muhammad','Kulit','081234567890'),
	('Samsul arip','Kebidanan','081234567890'),
	('Rahmad toyota','Paru paru','081234567890'),
	('Agus butterfly','Liver','081234567890'),
	('Sigit rendang','Poli umum','081234567890'),
	('Joko Miyako','Poli umum','081234567890'),
	('Ijat Pemda bogor','Spesialis anak','081234567890'),
	('Sigit rendang','Poli umum','081234567890'),
	('Mahmud','Jantung','081234567890');
	
SELECT*from Dokter;	
