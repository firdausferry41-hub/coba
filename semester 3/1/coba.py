
class TransaksiKasir:
    def __init__(self, pelanggan, barang, harga_satuan, jumlah):
        if harga_satuan <= 0 or jumlah <= 0:
            raise ValueError("Harga dan jumlah harus positif!")

        self.pelanggan = pelanggan
        self.barang = barang
        self.harga_satuan = harga_satuan
        self.jumlah = jumlah

    def hitung_subtotal(self):
        return self.harga_satuan * self.jumlah

    def tentukan_diskon(self):
        subtotal = self.hitung_subtotal()

        if subtotal >= 500000:
            return 0.15
        elif subtotal >= 250000:
            return 0.10
        elif subtotal >= 100000:
            return 0.05
        else:
            return 0

    def hitung_total(self):
        subtotal = self.hitung_subtotal()
        diskon = self.tentukan_diskon()
        potongan = subtotal * diskon
        return subtotal - potongan

    def tampilkan_struk(self):
        subtotal = self.hitung_subtotal()
        diskon = self.tentukan_diskon()
        potongan = subtotal * diskon
        total = self.hitung_total()

        print("\n=== STRUK PEMBAYARAN ===")
        print(f"Pelanggan   : {self.pelanggan}")
        print(f"Barang      : {self.barang}")
        print(f"Subtotal    : Rp{subtotal:,.0f}".replace(",", "."))
        print(f"Diskon      : {diskon:.0%}")
        print(f"Potongan    : Rp{potongan:,.0f}".replace(",", "."))
        print(f"Total bayar : Rp{total:,.0f}".replace(",", "."))
        print("========================")


# Program utama
try:
    pelanggan = input("Nama pelanggan: ")
    barang = input("Nama barang: ")
    harga = int(input("Harga satuan: Rp"))
    jumlah = int(input("Jumlah barang: "))

    transaksi = TransaksiKasir(
        pelanggan, barang, harga, jumlah
    )
    transaksi.tampilkan_struk()

except ValueError as e:
    print("Input tidak valid:", e)
