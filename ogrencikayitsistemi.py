#Bu öğrenci kayıt sistemine;    
#Aldığı isim soy isim ile listeye öğrenci ekleyen
#Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
#Listeye birden fazla öğrenci eklemeyi mümkün kılan
#Listedeki tüm öğrencileri tek tek ekrana yazdıran
#Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
#Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
#fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.
#Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir.
def addNameSurnameToList(information:str,list:list):
    list.append(information)
    return list
def deleteNameSurnameToList(information:str,list:list):
    list.remove(information)
    return list
def multipleInsertion(information:list,list:list):
    list.extend(information)
    return list
def printStudents(list:list):
    i=0
    while i<len(list):
        print(list[i])
        i+= 1
def getByNameSurname(information:str,list:list):
    indexStudent = list.index(information)
    print(f"{information} öğrencisinin numarası: {indexStudent}")
def multipledelete(students:list, list:list):
    for student in students:
        list.remove(student)
        
students= ["Ersin Yurtseven","Ali Yılmaz","Örnek Öğrenci"]
print("Öğrenci kayıt sistemine hoş geldiniz.")
while True:
    hello = int(input("Lütfen yapılacak işlemin numarasını yazın Öğrenci Ekle(1)/ Öğrenci Sil (2)/ Birden Fazla öğrenci Ekle(3)/ Öğrencileri Yazdır(4)/ Öğrencinin Numarasını Getir(5)/ Birden Fazla Öğrenci sil(6)/ Çıkış Yap(7) :"))
    if(hello == 1):
        student= input("Eklenecek öğrencinin adını ve soyadını girin: ")
        students= addNameSurnameToList(student,students)
    elif(hello ==2):
        student= input("Silinecek öğrencinin adını ve soyadını girin: ")
        students= deleteNameSurnameToList(student,students)
    elif(hello==3):
        addstudents=input("Eklenecek öğrencileri & işaretiyle ayırarak yazın: ")
        addstudentslist=addstudents.split('&')
        students= multipleInsertion(addstudentslist,students)
    elif(hello==4):
        printStudents(students)
    elif(hello==5):
        student= input("Numarası getirilecek öğrencinin adını ve soyadını girin: ")
        getByNameSurname(student,students)
    elif(hello==6):
        deletestudents= input("Silinecek öğrencileri & işaretiyle ayırarak yazın: ")
        deletestudentlist=deletestudents.splitlines("&")
        students= multipledelete(deletestudentlist,students)
    elif(hello==7):
        break
    else:
        print("Hatalı seçim yaptınız")
print("Kayıt edilmeyen değişiklikler silindi.")









