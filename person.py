class Person:
  #  def __init__(self) -> None:
  #      pass
    def __init__(self,name,lasName):
        self.name=name
        self.lastName=lasName

musteri1 = Person("Ali","Taş")
musteri2 = Person("Veli","Toprak")
musteri3 = Person("Selim","Duman")
print(musteri1.name)