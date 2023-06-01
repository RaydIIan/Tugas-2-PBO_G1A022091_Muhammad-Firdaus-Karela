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


### Buatlah sebuah objek Universitas dengan nama "XYZ University".

universitas_xyz = Universitas("XYZ University")

### Buatlah objek Jurusan dengan nama "Teknik Informatika" dan tambahkan objek tersebut ke dalam Universitas XYZ. 

# Membuat objek jurusan
jurusan_ti = Jurusan("Teknik Informatika")

# Menambahkan objek jurusan ke dalam objek universitas
universitas_xyz.tambah_jurusan(jurusan_ti)

### Buatlah objek Mahasiswa dengan nama "Kalian masing", NIM "Kalian masing", dan masukkan ke dalam Jurusan Teknik Informatika di Universitas XYZ.

# Membuat objek mahasiswa
mahasiswa_kalian = Mahasiswa("Kalian masing", "Kalian masing", jurusan_ti)

# Menambahkan objek mahasiswa ke dalam objek jurusan
jurusan_ti.tambah_mahasiswa(mahasiswa_kalian)

### Tampilkan daftar jurusan yang ada di Universitas XYZ.

universitas_xyz.tampilkan_daftar_jurusan()

### Tampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ.

jurusan_ti.tampilkan_daftar_mahasiswa()
