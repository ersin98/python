class Matematik:
    def __init__(self,sayi1,sayi2) -> None:#constructor- yapıcı
        self.sayi1= sayi1
        self.sayi2 =sayi2
        #pass
        print("matematik başladı(referansı oluştu)")
    def topla(self):
        return self.sayi1+ self.sayi2
    def cikar(self):
        return self.sayi1- self.sayi2
    def bol(self):
        return self.sayi1/ self.sayi2
    def carp(self):
        return self.sayi1* self.sayi2

matematik = Matematik(1,1)
sonuc= matematik.topla()
print(f"sonuç : {sonuc}")

class Istatistik(Matematik):
    def __init__(self, sayi1, sayi2):#-> None
        super().__init__(sayi1, sayi2)
    def varyansHesapla(self):
        return self.sayi1 * self.sayi2
    
Istatistik= Istatistik(5,0)