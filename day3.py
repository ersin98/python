

from human import Human


person = Human("Ersin")
person.name= " "#set edilmez ilse varsayılan kalır
person.talk("Merhaba")

person2= Human("Ersin")
person2.talk("Merhaba")
print(person2)

Human("İsim").talk("söylenecek")