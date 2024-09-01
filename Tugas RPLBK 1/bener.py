class Bentuk:
    def get_luas(self):
        pass

class PersegiPanjang(Bentuk):
    def __init__(self, lebar, tinggi):
        self._lebar = lebar
        self._tinggi = tinggi

    def set_lebar(self, lebar):
        self._lebar = lebar

    def set_tinggi(self, tinggi):
        self._tinggi = tinggi

    def get_luas(self):
        return self._lebar * self._tinggi

class Persegi(Bentuk):
    def __init__(self, sisi):
        self._sisi = sisi

    def set_sisi(self, sisi):
        self._sisi = sisi

    def get_luas(self):
        return self._sisi * self._sisi

def cetak_luas(bentuk: Bentuk):
    print(f"Luas: {bentuk.get_luas()}")

# Contoh penggunaan
persegi_panjang = PersegiPanjang(5, 10)
persegi = Persegi(4)

cetak_luas(persegi_panjang)  # Mencetak 50 dengan benar
cetak_luas(persegi)          # Mencetak 16 dengan benar


'''
Dalam kode ini baik (PersegiPanjang) maupun (Persegi) adalah subclass dari kelas abstrak Bentuk. Masing-masing kelas bentuk memiliki metode get_luas sendiri, 
dan tidak ada kebutuhan untuk menimpa metode set_lebar atau set_tinggi di (Persegi) karena sudah dikelola di proses yang berbeda.

Program ini menigkuti LSP karena sekarang baik (PersegiPanjang) maupun (Persegi) adalah bentuk yang berbeda dengan implementasi get_luas mereka sendiri. 
Kita bisa mengganti Bentuk dengan (PersegiPanjang) atau (Persegi) dalam fungsi cetak_luas yang mana hal itu akan berfungsi dengan benar.

'''