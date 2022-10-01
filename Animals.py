class Hayvanlar:
    def __init__(self,bacak_sayisi = 4,yasam_alani = "Kara",kosma_durumu = "Koşabilir",beslenme ="Otobur"):
        self.bacak = bacak_sayisi
        self.yasam_alani = yasam_alani
        self.kosma_durumu = kosma_durumu
        self.beslenme = beslenme
    
    def bilgiler(self):
        print("Bu hayvan {} bacağa sahiptir \n{}da yaşar \nKoşma durumu: {} \nBeslenme durumu: {}".format(self.bacak,self.yasam_alani,self.kosma_durumu,self.beslenme))

class Maymun(Hayvanlar):

    def bilgiler(self):
        super().bilgiler()
        print("Bu hayvan genetik olarak insana en yakın olan canlıdır, ağaçlara tırmanabilir ve ortalama 45-55 kg'dır.")

class At(Hayvanlar):

    def bilgiler(self):
        super().bilgiler()
        print("Bu hayvan hızlı koşabilir ve Türk devletlerinde kutsal kabul edilir.")

class Fil(Hayvanlar):

    def bilgiler(self):
        super().bilgiler()
        print("Bu hayvan karada yaşayan en büyük canlıdır ve ağırlıkları 7.000 kg'a kadar çıkabilir.")

