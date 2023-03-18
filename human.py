class Human:
    name="Ersin"
    def __init__(self,name) :
        self.name=name
        print("BİR HUMAN NESNESİ ÜRETİLDİ")
    def __str__(self):
        return f"STR  Fonksiyonundan dönene değer : {self.name}"
    def talk(self,sentence):
        name="bu kullanılmayacak"
        print(f"{self.name}:{sentence}")
    def walk(self):
        print("Human is walking")