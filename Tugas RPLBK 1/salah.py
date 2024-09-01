class PersegiPanjang:
    def __init__(self, lebar, tinggi):
        self._lebar = lebar
        self._tinggi = tinggi

    def set_lebar(self, lebar):
        self._lebar = lebar

    def set_tinggi(self, tinggi):
        self._tinggi = tinggi

    def get_luas(self):
        return self._lebar * self._tinggi

class Persegi(PersegiPanjang):
    def set_lebar(self, lebar):
        self._lebar = lebar
        self._tinggi = lebar

    def set_tinggi(self, tinggi):
        self._lebar = tinggi
        self._tinggi = tinggi

def cetak_luas(bentuk: PersegiPanjang):
    bentuk.set_lebar(5)
    bentuk.set_tinggi(10)
    print(f"Luas: {bentuk.get_luas()}")

# Contoh penggunaan
persegi = Persegi(4, 4)
cetak_luas(persegi)  # Ini akan mencetak 100, yang salah

'''
Dalam contoh di atas, kelas (Persegi) mewarisi dari kelas (PersegiPanjang). Maka secara teknis, (persegi) adalah (persegi panjang), tetapi dalam implementasi ini, 
metode set_lebar dan set_tinggi di Persegi mengakibatkan hasil yang tidak seharusnya diinginkan. Ketika fungsi cetak_luas mengatur lebar menjadi 5 dan tingginya menjadi 10, 
diharapkan luasnya menjadi 50. Akan tetapi sebaliknya, hasilnya adalah 100 karena baik lebar maupun tinggi pada persegi diatur menjadi 10.
Hal tersebut melanggar LSP karena menggantikan PersegiPanjang dengan Persegi menyebabkan program menghasilkan hasil yang salah.

'''