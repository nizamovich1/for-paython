# """Matini kesib chiqarish"""
# a = "Hello World!"
# print(a[:5])

# a = "Hello World!"
# print(a[2:])

# a = "Hello World!"
# print(a[-5:-2])

# """replace()"""
# b = "Hello, World, olma, gilos, olcha"
# print(b.replace("o", "-", 2))

# """split()"""
# b = "Hello, World, olma, gilos, olcha"
# print(b.split("m"))
 
"""Maxsus belgilar"""

# \'    'belgisi uchun
# \"    "belgisi uchun
# \n     yangi qator
# \r     yangi uchun
# \t     tab tashlab beradi uchun
# \b     boshliqni yoqotib beradi uchun

# """09.09.2024"""

# """Sonlarning turlari"""
# x = 1
# y = 2.8
# z = 1j

# print(type(x))
# print(type(y))
# print(type(z))

# """butun son turlari"""
# a = 15
# a = -8
# c = 0
# print(a)
# print(type(a))

# """o'nlik son turlar"""

# x = 35e4
# y = 12e3
# z = 14.76

# print(z)
# print(type(z))

# a = 5
# b = 7

# print(a+b)
# print(a-b)
# print(a/b)
# print(a*b)

# c = a+(b-7)*b
# print(c)

# """Sonni kvadratga ko'tarish"""
# from math import pow
# print(pow(3, 3))

# f = 3**4
# print(f)

# """Soning ildizi"""
# d = 16
# from math import sqrt 
# print(sqrt(d))


# """soning yaxlidlash"""
# print(round(4.225, 2))
# print(round(4.225))

# """int()/ str()/ float()"""
# a = 5
# b = 12.3
# c = "Salom"

# print(type(a))
# print(a)
# a1 = float(a)
# print(type(a1))
# print(a1)

# """Bir vaqting ozida bir necha ozgaruvchi yaratish"""
# x,y,z = 4,9,-7
# print(x,y,z)

# """kop honali sonlar"""
# uzb = 36_032_123
# yer = 800_321_215_245
# print(yer)
# print(uzb)


"""12.09.2024"""
# ism = ["Mansur", "Qobil", "Islom", "Otabek"]
# print(f"Salom {ism[1]} o't yedingmi")
# print(f"Salom {ism[0]} nma gap")
# print(f"Salom {ism[2]} otni kurdingmi")
# print(f"Salom {ism[-1]} bugun kelasanmi")

# son = [2, -1, 12.42, 832, -63]
# print(son[-1] * son[0])
# print(son[1] + son[0])
# print(son[2] - son[-2])
# son[-1] = 63
# print(son)

"""16.09.2024"""
# fruts = ["apple", "banana", "cherry"]
# tropic = ["mango", "pineapple", "papaya"]

# fruts.extend(tropic)
# print(fruts)

# del fruts[1]
# print(fruts)

# fruts.remove("apple")
# print(fruts)
 
# fruts.pop(3)
# print(fruts)

# fruts = ["apple", "banana", "cherry"]
# print(f"Bizning vazada {len(fruts)}-ta meva bor")
# print(f"Ular {fruts[0]}, {fruts[1]}, {fruts[2]}")

# fruts = ["apple", "banana", "cherry"]
# fruts.clear()
# print(fruts)

# """1-mashq"""
# aktorlar = ["Ulugbek", "Ozodbek", "Munisa", "Rayxon", "Vali"]
# aktorlar1 = ["Ulugbek Raxmatilo", "Ozodbek Nazarxon", "Munisa Rizayeva", "Ravzaxon", "ali"]
# print(aktorlar)
# print(aktorlar1)
# del aktorlar[0]
# del aktorlar[1]
# del aktorlar1[0]
# del aktorlar1[1]
# print(aktorlar)
# print(aktorlar1)

# insonlar = []
# insonlar.extend(aktorlar1)
# insonlar.extend(aktorlar1)
# print(insonlar)

"""17.09.2024"""
# mexmonlar = []
# mexmonlar.append("Ali")
# mexmonlar.append("Alisher")
# mexmonlar.append("Alixon")
# mexmonlar.append("Mansurxon")
# mexmonlar.append("MuxammadAli")
# print(mexmonlar)

# mexmonlar.remove("MuxammadAli")
# mexmonlar.remove("Ali")
# mexmonlar.remove("Alisher")
# print(f"{len(mexmonlar)} kela oladi, Ular")
# print(f"{mexmonlar[0]}, {mexmonlar[1]}")

"""range()"""
# son = list(range(60, 100))
# son1 = son[10:]
# print(son)
# print(son1)



# aktorlar = ["Ulugbek", "Ozodbek", "Munisa", "Rayxon", "Vali"] 
# print(aktorlar)
# aktorlar.sort()
# print(aktorlar)

# print(sorted(aktorlar))

# aktorlar.reverse()
# print(aktorlar)


# """19.09.2024      """
# son = [1, 4, 134, 544, 232, 0, -5434, 132]
# print(son)
# son.sort()
# print(son)
# print(f"Shu sonlarning eng kattasi {max(son)} eng kichigi {min(son)}")

# davlat = ["Amerika", "AQSH", "Buyuk britaniya", "Qoraqalpagistan", "Uzbekistan", "Namangan", "Toshkent"]
# print(len(davlat))
# print(sorted(davlat))
# print(sorted(davlat, reverse=True))
# print(davlat)
# davlat.reverse()
# print(davlat)
# davlat.sort()
# print(davlat)
# davlat.sort(reverse=True)
# print(davlat)

# """2-mashq"""
# son = list(range(120, 1200, 2))    
# print(sum(son))
# print(f"Shu sonlarning eng kattasi {max(son)} eng kichigi {min(son)}")
# print(len(son))
# son1 = son[:20]
# print(son1)
# son1 = son[260:280]
# print(son1)
# son1 = son[520:540]
# print(son1)

"""3-mashq"""
# taomlar = ["Qotirma", "Osh", "Mastava", "Qaymoq", "Sariyoq"]
# nonushta = []
# nonushta = taomlar.copy()
# print(nonushta)
# del nonushta[0]
# del nonushta[1]
# del nonushta[2]
# print(nonushta)
# nonushta.append("Coffe")
# nonushta.append("Shashlik")
# print(nonushta)

# taomlar = ["Qotirma", "Osh", "Mastava", "Qaymoq", "Sariyoq"]
# for taom in taomlar:
#     print(f"Mening eng sevimli taomim {taom}")
# print("Lekin men ovqat tanlamayman")

# for s in range(1, 102):
#     print(f"{s}-chi ")
 
# ism = "Mansurxon"
# for i in ism:
#     print(i)

# for s in range(1, 101):
    # print(f"{s}- {s**2}")


"""1-mashq"""
# ism = ["Olim", "Ali", "Vali", "Nuri", "Shuri"]
# for i in ism:
#     print(f"Salom {i} nma gap")
#     print(f"Kod {ism} marta takrolandi")

"""2-mashq"""
# son = list(range(11, 100, 2))
# for s in son:
#     print(f"{s}-Shu soning kubi va kavadrati mos ravishda {s**2}, {s**3}")
#     print(f"{s}-Shu soning 1 ga kichigi va 3 ga kattasi mos ravishda {s-1}, {s+3}")
                
"""3-mashq"""
# kinolar = []

# for i in range(5):
#     kino = input(f"{i + 1}-sevimli kinongizni kiriting: ")
#     kinolar.append(kino)

# print("\nSevimli kinolaringiz:")
# for kino in kinolar:
#     print(f"- {kino}")

# """4-mashq"""
# # foydalanuvchi bugun nechta odam bilan suxbatlashganini sorang va har bir suxbatlashgan odamini sorab royxatga yozing
# kino = []
# son = int(input("Necha odam bilan gaplashdingiz: "))
# for s in range(son):
#     a = input("Ularni ismini krting: ")
#     kino.append(a)
# print(kino)

"""24.09.2024"""
# ismlar = ["Olim", "Vali", "Shali", "Salim", "Nuri", "Shuri"]
# for ism in ismlar:
#     if ism == "Shuri":
#         print(f"Salom {ism}, yaxshimisan")
#     else:
#         print(f"Salom {ism}")

# sonlar = int(input("1 dan 10 gacha bolgan soni krting: "))
# if sonlar > 10 or sonlar <= 0:
#     print("Xatolik qaytadan uruning !!!") 
# elif sonlar < 5:
#     print(f"{sonlar} Bu son 5 dan kichik")
# elif sonlar == 5:
#     print(f"{sonlar} bu son 5 ga teng")
# elif sonlar > 5:
#     print(f"{sonlar} Bu son 5 dan katta")

"""1-mashq"""

# son = int(input("soni krting: "))
# son1 = int(input("soni krting: "))
# if son < son1:
#     print(f"{son} < {son1}")
# elif son > son1:
#     print(f"{son} > {son1}")
# elif son == son1:
#     print(f"{son} == {son1}")

"""2-mashq"""

# ismlar = ["Olim", "Vali", "Shali", "Salim", "Nuri", "Shuri"]
# for ism in ismlar:
#     if ism == "Vali" or ism == "Shali":
#         print(f"Salom {ism} axvoling yaxshimi")
#     else:
#         print(f"Assalomu aleykum {ism}")

# ismlar = ["olim", "vali", "shali", "salim", "nuri", "shuri"]
# for ism in ismlar:
#     if ism == "olim" or ism == "shali":
#         print(f"{ism.upper()} Salom")
#     else:
#         print(f"{ism.title()} salom")

# son = list(range(205, 2024))
# for s in son:
#     if s <= 1000:
#         print(f"{s} < 1000")
#     elif s > 1500:
#         print(f"{s}-3 ={s-3} ")
#     if s%25 ==0:
#         print(f"{s}%25 = qoldiq(0)")

"""25.06.24"""
# son = int(input("Son krting:"))
# if son > 0:
#     if son%2 == 0:
#         print(f"{son} bu son juft va musbat")
# elif son < 0:
#     if son%2 == 1:
#         print(f"{son} bu son toq va manfiy")


# son = int(input("Son krting:"))
# if son > 0:
#     if son%2 == 0:
#         print(f"{son} bu son juft va musbat")
#     elif son%2 != 0:
#         print(f"{son} bu son toq va musbat")
# elif son < 0 :
#     if son%2 == 0:
#         print(f"{son} bu son juft va manfiy")
#     elif son%2 == 1:
#         print(f"{son} bu son toq va manfiy")

# ball = int(input("Necha baxo oldingiz: "))
# if ball == 5:
#     print("Siz allo baxo oldingiz: ")
# elif ball == 4:
#     print("yaxshi")
# elif ball == 3:
#     print("qoniqarli")
# elif ball == 2:
#     print("qoniqarsz")
# elif ball == 1:
#     print("yomon")
# elif ball == 0:
#     print("ota yomon ")
# if ball > 5 or ball< 0:
#     print("Xatolik")

"""26.09.2024"""
"""1-mashq"""
# maxsulotlar = ["olma", "nok", "shaptali", "bexi"]
# bor_maxsulotlar = []
# yoq_maxsulotlar = []

# sotib = int(input("Necha mahsulot sotib olmoqchisiz: "))
# for s in range(sotib):
#     a = input("Ular nomini krting: ")
#     if a in maxsulotlar:
#         print(f"{a} bu bizda bor"bor_maxsulotlar.append(a))
#     elif a not in maxsulotlar:
#         print(f"{a} bizda yoq".append(yoq_maxsulotlar))

# yosh = int(input("Yoshingizni krting: "))
# if yosh < 0 or yosh >100:
#     print("Adashdingiz ")
# elif yosh > 7 and yosh <=18:
#     print("Szga krish 5 ming so'm")
# elif yosh > 18 and yosh <= 69:
#     print("Szga krish 10 ming so'm")
# else:
#     print("Szga bepul")

# cars = ["toyota", "lexus", "gm", "kia", "monza"]
# for car in cars:
#     if car != "gm":
#         print(f"{car.title()}")
#     else:
#         print(car.upper())

# from math import sqrt
# son1 = int(input("Son krting: "))
# son2 = int(input("Son krting: "))
# son = son1, son2
# for s in son:
#     if s > 0:
#         print(sqrt(s))
#     else:
#         print("Musbat son krting: ")

# parol = input("Parol krting: ")
# if len(parol) >= 8:
#     parol1 = input("Qaytadan krting: ")
#     if parol1 == parol:
#         print("Parol muvofaqiyatli ornatildi")
#         p = input("tizimga Qaytadan krting:")
#         if p == parol1:
#             print("Xush kelibsz")
#         else:
#             print("Xatolik")
#     else:
#         print("2-chi parol xato")
# else:
#     print("Parol 8 tadan kop xarf ishlatilsin !!!")
    
# yosh = int(input("Yoshingizni krting: "))
# if yosh == 15:
#     jins = input("Jinsingizni krting: ")
#     if jins == "ogil":
#         print("Sz 9-blue snfiga qabul qilindingiz ")
#     if jins == "qiz":
#         print("Sz 9-green snfiga qabul qilindingiz")
# else:
#     print("Kechirasz bz faqat 15 yoshga yetganlarni krtamz")
    


# ism = input("Ismingizni krting: ")
# if bool(ism):
#     print("raxmat")
# else:
#     print("hech narsa krtmadingiz")
        
"""03.10.24"""
# ism = {"Ali":"osh",
#        "Vali":"Norin",
#        "Axmad":"shashlik",
#        "Mansur":"qotirma",
#        "Sali":"mastava"

# }
# ism.update({"Axror":"shorva"})
# ism["Karim"] = '5 barmoq'
# ism["Kari"] = input("Sevimli oqatingizni krting: ")
# print(ism)

# del ism["Ali"]
# print(ism)
# ism.pop("Ali")
# print(ism)
# ism.popitem()
# print(ism)

# otam = {"ism":"nizom",
#         "yosh":43,
#         "manzil":"namangan",
#         "boy":1.70
        
#         }
# print(f"Mening otamning ismi {otam["ism"]}, yoshi {otam["yosh"]}, tugilgan manzili {otam["manzil"]} va boyi {otam["boy"]}")

# """2-mashq"""
# ism = {"Ali":"osh",
#        "Vali":"Norin",
#        "Axmad":"shashlik",
#        "Mansur":"qotirma",
#        "Sali":"mastava"

# }
# python = {"if":"agar",
#           "else":"bolmasa",
#           "list":"royxat",
#           "int":"butun son",
#           "str":"lug'at",
#           "float":"o'nlik son",
#           "input":"qoshmoq",
#           "in":"ichida",
#           "not in":"ichida yoq"

# }

# """3-mashq"""
# fanlar = {"Muxammadzoxor":"Matem",
#           "Javlon":"Tarix"


"""07.10.2024"""
# ism = {"Ali":"osh",
#        "Vali":"Norin",
#        "Axmad":"shashlik",
#        "Mansur":"qotirma",
#        "Sali":"mastava"}
# ismlar = {}
# ismlar = ism.copy()
# print(ismlar)

# ismlar = dict(ism)
# print(ismlar)

# ism = {"Ali":"osh",
#        "Vali":"Norin",
#        "Axmad":"shashlik",
#        "Mansur":"qotirma",
#        "Sali":"mastava"}

# # print(f"Salom, {ismlar["ali"]}")

# print(f"Salom, {ismlar.get("ali", "51")}")

# print(ismlar)
# print(ismlar.items())
# for key, value in ismlar.items():
#     print(f"{key.title()} ning sevimli ovqati {value.capitalize()}")


"""14.10.2024"""
"""1-mashq"""
# taom = {"osh":15000,
        # "manti":20000,
        # "shorva":16000,
        # "shashlik":14000,
        # "qotirma":18000,
        # "dimlama":22000,
        # "kabob":27000,
        # "5 barmoq":52000
        # 
        # }
# 
# buyurtma =input("ovqat Nomini krting: ")
# buyurtma1 =input("ovqat Nomini krting: ")
# buyurtma2 =input("ovqat Nomini krting: ")
# b = buyurtma1, buyurtma, buyurtma2
# for k, v in taom.items():
    # if k == buyurtma:
        # print(f"{buyurtma}-{v}")
    # if k == buyurtma1:
        # print(f"{buyurtma1}-{v}")
    # if k == buyurtma2:
        # print(f"{buyurtma2}-{v}")
# if k not in b:
    # print(f"bizda bu taomlar yoq")


# while  True:
#     son = int(input("Son krting biz kvadratini chiqazamz: "))
#     print(f"{son} ning kvadrati {son**2} ga teng")
#     savol = input("Dastur davom etsunmi {yes/no}: ")
#     if savol == "yes":
#         continue
#     elif savol == "no":
#         print("Dastur toxtatildi")
#         break
#     else:print("Eror !")

"""mashq"""
while True:
    yil = int(input("Tug'ilgan yilingizni krting: "))
    print(f"Sz {2024-yil} yoshsz")
    savol = input("Davom etiraymi {exit/}: ")
    if savol == "exit":
        break
    else:
        continue
    
