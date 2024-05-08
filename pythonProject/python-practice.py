# Görev 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz,
# kelime kelime ayırınız.

text = "The goal is to turn data into information, and information into insight."

text = text.upper()
text = text.replace('.', '').replace(',', '')
new_list = text.split()

# Görev 3: Verilen listeye aşağıdaki adımları uygulayınız

lst = list("datascience".upper())

# Adım 1: Verilen listenin eleman sayısına bakınız.
len(lst)

# Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
lst[0], lst[10]

# Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
range(0, 4)
new_lst = lst[0: 4]

# Adım 4: Sekizinci indeksteki elemanı siliniz.
lst.remove(lst[8])
lst.pop(8)

# Adım 5: Yeni bir eleman ekleyiniz.
lst.append('126')

# Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.
lst.insert(8, 'N')

# Görev 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.

dict = {
    'Christian': ['America', 18],
    'Daisy': ['England', 12],
    'Antonio': ['Spain', 22],
    'Dante': ['Italy', 25]}

# Adım 1: Key değerlerine erişiniz.
dict.keys()

# Adım 2: Value'lara erişiniz.
dict.values()

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
dict.update({"Daisy": ['England', 13]})
dict["Daisy"][1] = 14
dict.get('Daisy')[1] = 15

# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
dict.update({'Ahmet': ['Turkey', 24]})

# Adım 5: Antonio'yu dictionary'den siliniz.
dict.pop('Antonio')

# Gorev 5: Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve
# bu listeleri return eden fonksiyon yazınız.
lst = [2, 13, 18, 93, 22]


def func(list):
    odd_list = []
    even_list = []
    for value in list:
        if value % 2 == 0:
            even_list.append(value)
        else:
            odd_list.append(value)
    return even_list, odd_list


def func2(list2):
    """

    Parameters
    ----------
    list2

    Returns
    -------
    in order returned even and odd list.

    """
    even_lst = [x for x in list2 if x % 2 == 0]
    odd_lst = [x for x in list2 if x % 2 != 0]
    return even_lst, odd_lst


even_list, odd_list = func2(lst)

# Görev 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri
# bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de
# tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
students = ["Ali", "Veli", "Ayse", "Talat", "Zeynep", "Ece"]


def funct(students_list):
    index2 = 0
    for index, student in enumerate(students):
        if index < 3:
            index += 1
            print("Faculty of Engineering", index, ". student:", student)
        else:
            index2 += 1
            print("Faculty of Engineering", index2, ". student:", student)


funct(students)

# another solution
# enumerate(iterable, startIndex)
[print("Faculty of Engineering{}. student: {}".format(index, value)) if index < 4
 else print("Faculty of Engineering{}. student: {}".format((index - 3), value))
 for index, value in enumerate(students, 1)]

# Görev 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri
# yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

zip(ders_kodu, kredi, kontenjan)
for a, b, c in zip(kredi, ders_kodu, kontenjan):
    print("Kredisi {} olan {} kodlu dersin kontenjani {} kisidir.".format(a, b, c))

# Görev 8: Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını
# eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
set1 = set(["data", "python"])
set2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])


def func3(set1, set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))


func3(set1, set2)




