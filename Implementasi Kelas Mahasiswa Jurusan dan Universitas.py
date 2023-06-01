#Implementasikan kelas Mahasiswa, Jurusan dan Universitas sesuai dengan spesifikasi yang diberikan.

class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_info(self):
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Jurusan:", self.jurusan.nama_jurusan)


class Jurusan:
    def __init__(self, nama_jurusan):
        self.nama_jurusan = nama_jurusan
        self.daftar_mahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.daftar_mahasiswa.append(mahasiswa)

    def tampilkan_daftar_mahasiswa(self):
        print("Daftar Mahasiswa di Jurusan", self.nama_jurusan)
        for mahasiswa in self.daftar_mahasiswa:
            mahasiswa.tampilkan_info()
            print()


class Universitas:
    def __init__(self, nama_universitas):
        self.nama_universitas = nama_universitas
        self.daftar_jurusan = []

    def tambah_jurusan(self, jurusan):
        self.daftar_jurusan.append(jurusan)

    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di Universitas", self.nama_universitas)
        for jurusan in self.daftar_jurusan:
            print("Nama Jurusan:", jurusan.nama_jurusan)


# Contoh penggunaan program

# Membuat objek jurusan
jurusan_ti = Jurusan("Teknik Informatika")
jurusan_tk = Jurusan("Teknik Komputer")

# Membuat objek mahasiswa
mahasiswa1 = Mahasiswa("Andi", "123456", jurusan_ti)
mahasiswa2 = Mahasiswa("Budi", "789012", jurusan_ti)
mahasiswa3 = Mahasiswa("Cindy", "345678", jurusan_tk)

# Menambahkan mahasiswa ke dalam daftar mahasiswa pada jurusan
jurusan_ti.tambah_mahasiswa(mahasiswa1)
jurusan_ti.tambah_mahasiswa(mahasiswa2)
jurusan_tk.tambah_mahasiswa(mahasiswa3)

# Membuat objek universitas
universitas_xyz = Universitas("XYZ")
universitas_xyz.tambah_jurusan(jurusan_ti)
universitas_xyz.tambah_jurusan(jurusan_tk)

# Menampilkan informasi mahasiswa dan jurusan
jurusan_ti.tampilkan_daftar_mahasiswa()
jurusan_tk.tampilkan_daftar_mahasiswa()

universitas_xyz.tampilkan_daftar_jurusan()
