class çalışan_bilgi:
    def __init__(self,ad ="Emre",soyad = "YILDIRIM",maaş = 7500,zam = 500):
        self.ad = ad
        self.soyad = soyad
        self.__maaş = maaş
        self.__zam = zam

    def bilgiler(self):
        print("Kişinin adı: {} \nKişinin soyadı: {}".format(self.ad,self.soyad))

    def get_maaş(self):
        print("{} {}, {} dolar maaş alıyor.".format(self.ad,self.soyad,self.__maaş))
    
    def set_maaş(self):
        self.__maaş += self.__zam

    def get_zam(self):
        print("{} {}, bir sonraki ay {} dolar zam alacak".format(self.ad,self.soyad,self.__zam))
    
    def set_zam(self,yeni_zam):
        self.__zam = yeni_zam


    

