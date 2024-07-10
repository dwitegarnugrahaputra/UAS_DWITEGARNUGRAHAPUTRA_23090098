#parent class
class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def information(self):
        return f"nama: {self.nama}, warna: {self.warna}, rasa: {self.rasa}"
#child class
class mangga(Buah):
    def __init__(self, nama, warna, rasa, vitamin):
        super().__init__(nama, warna, rasa)
        self.vitamin = vitamin

    def information(self):
        return f"{super().information()}, vitamin: {self.vitamin}"
    
mangga1 = mangga("mangga harum manis", "hijau", "manis", "vitamin C")
print(mangga1.information())

mangga1.nama = "mangga Gedong"
mangga1.warna = "Kuning"
mangga1.rasa = "manis dan Sedikit Asam"
mangga1.vitamin = "vitamin A dan C"
print(mangga1.information())
