#Veri Tipleri
#int= Tam sayıdır. Diğer dillerden farklı olarak negatif veya pozitif bir sınırı yoktur.
#float= Ondalıklı sayıdır.Bölme işlemlerinden tam sayı çıksa dahi otomatik olarak veri türü float verilir.
#str= metinsel veya karakter ifadeleri temsil eder. Çift tırnak içerisinde yazılır. 
#bool= Mantıksal ifadelerdir. True ve False olmak üzere iki değer alabilir.
#complex= Gerçek ve sanal sayılardan oluşur. Özellikle matematiksel hesaplamalarda ve bilimsel hesaplamalarda kullanılır. 
#list=Sıralı verileri depolamak için kullanılır. Veriler değiştirilebilir. Değiştirilemez hali için tuple kullanılır. 
#set= Benzersiz elemanları depolamak için kullanılır. Veriler değiştirilebilir. Değiştirilemez hali için frozenset kullanılır. 
#dict= Anahtar ve değer çiftlerini saklamaya yarar.
#bytes= Okunabilir ve değiştirilemez  byte dizisini ifade eder. Değiştirilebilir hali için bytearray kullanılır. Genellikle dosya ya da ağ üzerinden gelen veriler için kullanılırlar.
#memoryview = bellek üzerinde oluşturulacak bellek görünümü oluşturur. Bunlar bir dizi byte ı temsil eder ve üzerinde okuma ve yazma işlemi yapılabilir.
odevTanimi=str("Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.")
tamamlanmaOrani= int(75)
print("%",tamamlanmaOrani ,"TAMAMLANDI")

tamamlanmaIsareti=1
if(tamamlanmaIsareti==1):
    print("mavi tik")
elif(tamamlanmaIsareti==2):
    print("yarım tik")
else:
    print("boş")



