class BMI:
    def __init__(self, berat_pounds, tinggi_feet):
        self.berat = berat_pounds
        self.tinggi = tinggi_feet

    @property
    def berat(self):
        return self._berat
    
    @berat.setter
    def berat(self, berat_pounds):
        if berat_pounds <= 0:
            raise ValueError("Berat harus bernilai positif")
        self._berat = berat_pounds

    @property
    def tinggi(self):
        return self._tinggi
    
    @tinggi.setter
    def tinggi(self, tinggi_feet):
        if tinggi_feet <= 0:
            raise ValueError("Tinggi harus bernilai positif")
        self._tinggi = tinggi_feet

    def nilai_BMI(self):
        tinggi_meter = self.tinggi * 0.3048  # Konversi feet ke meter
        berat_kg = self.berat * 0.453592  # Konversi pounds ke kilogram
        bmi = berat_kg / (tinggi_meter ** 2)
        return bmi

    def __eq__(self, lainnya):
        if isinstance(lainnya, BMI):
            return self.berat == lainnya.berat and self.tinggi == lainnya.tinggi
        return False

# Definisi variabel
orang1 = BMI(150, 5.6) 
orang2 = BMI(170, 6.0)

print("BMI Orang 1:", orang1.nilai_BMI())
print("BMI Orang 2:", orang2.nilai_BMI())

print("Orang 1 dan Orang 2 memiliki berat dan tinggi yang sama:", orang1 == orang2)

