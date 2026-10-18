
class PenilaianMahasiswa:
    def __init__(self, nim, nama, tugas, uts, uas):
        self.nim = nim
        self.nama = nama

        if not all(0 <= nilai <= 100 for nilai in [tugas, uts, uas]):
            raise ValueError("Nilai harus antara 0 sampai 100!")

        self.tugas = tugas
        self.uts = uts
        self.uas = uas

    def hitung_nilai_akhir(self):
        return (self.tugas * 0.30) + (self.uts * 0.30) + (self.uas * 0.40)

    def tentukan_grade(self):
        nilai = self.hitung_nilai_akhir()

        if nilai >= 85:
            return "A"
        elif nilai >= 75:
            return "B"
        elif nilai >= 65:
            return "C"
        elif nilai >= 50:
            return "D"
        else:
            return "E"

    def tentukan_status(self):
        if self.hitung_nilai_akhir() >= 65:
            return "LULUS"
        else:
            return "TIDAK LULUS"

    def tampilkan_hasil(self):
        print("\n=== HASIL AKADEMIK ===")
        print(f"NIM         : {self.nim}")
        print(f"Nama        : {self.nama}")
        print(f"Nilai Akhir : {self.hitung_nilai_akhir():.2f}")
        print(f"Grade       : {self.tentukan_grade()}")
        print(f"Status      : {self.tentukan_status()}")
        print("======================")


# Program utama
try:
    nim = input("NIM           : ")
    nama = input("Nama          : ")
    tugas = float(input("Nilai Tugas   : "))
    uts = float(input("Nilai UTS     : "))
    uas = float(input("Nilai UAS     : "))

    mahasiswa = PenilaianMahasiswa(
        nim, nama, tugas, uts, uas
    )

    mahasiswa.tampilkan_hasil()

except ValueError as e:
    print("Input tidak valid:", e)
