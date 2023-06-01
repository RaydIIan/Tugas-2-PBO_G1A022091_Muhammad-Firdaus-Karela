#Implementasikan kelas Mahasiswa, Jurusan dan Universitas sesuai dengan spesifikasi yang diberikan.

class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_info(self):
        print("Nama: ", self.nama)
        print("NIM: ", self.nim)
        print("Jurusan: ", self.jurusan.NamaJurusan)


class Jurusan:
    def __init__(self, nama_jurusan):
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.DaftarMahasiswa.append(mahasiswa)

    def tampilkan_daftar_mahasiswa(self):
        print("Daftar Mahasiswa di Jurusan", self.NamaJurusan)
        for mahasiswa in self.DaftarMahasiswa:
            print("Nama: ", mahasiswa.nama)
            print("NIM: ", mahasiswa.nim)
            print()


class Universitas:
    def __init__(self, nama_universitas):
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []

    def tambah_jurusan(self, jurusan):
        self.DaftarJurusan.append(jurusan)

    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di Universitas", self.NamaUniversitas)
        for jurusan in self.DaftarJurusan:
            print("Nama Jurusan: ", jurusan.NamaJurusan)
            print()


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
