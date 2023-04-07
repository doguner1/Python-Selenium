
print("\n")
print("\n")
print("\nHoşgeldiniz\n")

loop = True
students = ["Melike Yazır","Yusuf Yazır","Hüveriya Gür","Sara Nazlı Gür","Fatoş Gür","Toprak Gür"
            ]

def menu():
    sec = input("Lütfen yapmak istediğiniz işlemi seçiniz: \n"
                "1  - Yeni Kayıt Oluştur \n"
                "2  - Var Olan Kaydı Sil \n"
                "3  - Kayıtları Listele  \n"
                "4  - Öğrenci Numarası Sorgula \n"
                "5  - Oturumu Kapat \n"
                "\n\n")

    if sec == "1":
        print("Kayıt ekleme menüsüne yönlendiriliyorsunuz..  \n")
        addStudents()
    if sec == "2":
        print("Kayıt silme menüsüne yönlendiriliyorsunuz.. \n")
        removeStudents()
    if sec == "3":
        print("Kayıtlar Listeleniyor.. \n")
        listStudents()
    if sec == "4":
        print("Öğrenci numarası sorgulama sayfasına gidiliyor.. \n")
        numStudents()
    if sec == "5":
        print("Oturum kapatılıyor.. \n")
        exit()
    if sec > "5":
        print("\nİşlem bulunamadı, lütfen tekrar deneyiniz.. \n"
                "Lütfen işleme ait rakamı giriniz..\n")
           
def addStudents():
    add = input("Eklemek istediğiniz öğrencinin adını ve soy adını giriniz: \n ")
    students.append(add)
    print(f"{add} başarıyla eklendi.".format())


   
def removeStudents():
 
    remove = input("\n Silmek istediğiniz kaydın ad ve soyadını giriniz  \n" )
    students.remove(remove)
    print(f"{remove} adlı kayıt silindi..".format())
  

     

def listStudents():
    for student in students:
        print(student, end='\n')
    menuReturn()
    
def numStudents():
    for student in students:
        print(student, end='\n')
    num = input("\n Numarasını öğrenmek istediğiniz öğrencinin adını ve soyadını giriniz \n")

    stuNum = students.index(num)
    print("{}'nın Numarası:  {}".format(num,stuNum))

def menuReturn():
    sec = input("\n Lütfen yapmak istediğiniz işlemi seçiniz: \n"
                "1 - Ana menüye dön \n"
                "2 - Oturumu kapat \n")
    if sec == "1":
        print("\n Ana menüye yönlendiriliyorsunuz")
        menu()
    if sec == "2":
        print(" \n Oturum kapatılıyor.")
        exit()

while loop:
    menu()
   
          
def exit():
    print("\n Sistemden çıkış yapılıyor..")             
    
        
    
            


        
            