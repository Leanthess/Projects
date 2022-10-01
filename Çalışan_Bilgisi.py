class çalışan_bilgi:
    def __init__(self,ad ="Emre",soyad = "YILDIRIM",maaş = 7500,çalışma_suresi_ay = 5):
        self.ad = ad
        self.soyad = soyad
        self.__maaş = maaş
        self.çalışma_suresi_ay = çalışma_suresi_ay

    def bilgiler(self):
        print("Kişinin adı: {} \nKişinin soyadı: {} \nKaç aydır çalışıyor: {} ay".format(self.ad,self.soyad,self.çalışma_suresi_ay))

    def get_maaş(self):
        print("Çalışan kişi {} dolar maaş alıyor.".format(self.__maaş))
    
    def toplam_alinan_para(self):
        print("Çalışan bu zamana kadar {} dolar maaş aldı.".format(self.çalışma_suresi_ay * self.__maaş))




