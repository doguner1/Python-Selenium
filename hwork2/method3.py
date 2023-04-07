students = ['Ali Demir', 'Orhan Veli', 'Peyami Sefa', "M", "Moniqi", "A", "B"]


def listStudents():
    for student in students:
        print()


def addStudent():
    print("\nEkle")
    name = input("ad giriniz : ")
    lastName = input("sayadi yaziniz : ")
    students.append(name + " " + lastName)
    print(name + " " + lastName + " isimli ogrenci eklendi\n")


def deleteStudent():
    print("Sil")
    name = input("ad giriniz : ")
    lastName = input("sayadi yaziniz : ")
    students.append(name + " " + lastName)
    if name in students:
        students.remove(name)
        print(name + " " + lastName + " isimli ogrenci silindi")
    else:
        print("Aranan isim bulunamadi..")


def addMultiStudents():
    print("\nCoklu Ekle")
    x = int(input("Kac adet ögrenci eklenecek  : "))
    i = 0
    while i < x:
        name = input("İsim yaz : ")
        lastName = input("sayadi yaziniz : ")
        students.extend(name + " " + lastName)
        i += 1

    print("ogrenciler eklendi\n")


def deleteMultiStudents():
    x = int(input("Kac adet ad silinecek : "))
    i = 0
    while i < x:
        name = input("ad giriniz : ")
        lastName = input("sayadi yaziniz : ")
        students.remove(name + " " + lastName)

        i += 1
    else:
        print(students)
