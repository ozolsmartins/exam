# import math
# class taisnsturis:
#     def __init__(self,a,b):
#         self.mala1=a
#         self.mala2=b
#     def laukums(self):
#         return self.mala1*self.mala2
#     def perimetrs(self):
#         return self.mala2*2+self.mala1*2


# x=int(input("ievadi malu 1"))
# y=int(input("ievadi malu 2"))
# t=taisnsturis(x,y)
# print(t.mala1)
# print(t.laukums())
# print(t.perimetrs())

# class cilindrs:
#     def __init__(self,r,h):
#         self.augstums1=h
#         self.radiuss1=r
#     def tilpums(self):
#         math.pi*self.r**2*self.augstums1
# class person:
#     def __init__(self,n,s,h,a):
#         self.name=n
#         self.surname=s
#         self.height=h
#         self.age=a
#     def vards(self):
#         return self.name+" "+self.surname
#     def augumsvards(self):
#         return self.name+" "+self.surname+" "+str(self.height)
# Martins=person("Martins","Ozols",190,17)
# print(Martins.name)

# class datums:
#     def __init__(self,d,m):
#         if d<1 or d>31:
#             print("datums nav pareizs")
#             self.diena=1
#         else:
#             self.diena=d
#         if m<1 or m>12:
#             print("menesis nav pareizs")
#             self.menesis=1
#         else:
#             self.menesis=m
#     def printdatums(self):
#         return str(self.diena)+" "+str(self.menesis)
#     def nakosadiena(self):
#         self.diena+=1
# a=datums(16,3)
# print(a.printdatums())
# a.nakosadiena()
# print(a.printdatums())

class laiks:
    def __init__(self,m,s):
        self.minutes=m
        if s<1 or s>59:
            print("sekundes nav pareizas")
            self.sekundes=1
        else:
            self.sekundes=s
    def nakosasekunde(self):
        if self.sekundes<59:
            self.sekundes+=1
        else:
            self.sekundes=0
            self.minutes+=1
    def printlaiks(self):
        return str(self.minutes)+":"+str(self.sekundes)
a=laiks(3,58)
a.printlaiks()
a.nakosasekunde()
a.printlaiks()
a.nakosasekunde()
a.printlaiks()
print(a.printlaiks())


class Subscription:
    def __init__(self,c):
        self.cena=c
    def monthly(self, month_count):
        return self.cena*month_count
spotify=Subscription(6.99)
print(spotify.monthly(12))

netflix=Subscription(11.99)
print(netflix.monthly(24))

disney=Subscription(7.99)
print(disney.monthly(36))

youtube=Subscription(11.99)
print(youtube.monthly(48))


class sekmjuizraksts:
    def __init__(self):
        self.sekmes=[]
    def atzime(self,a):
        if a>=1 and a<=10:
            self.sekmes.append(a)
        else:
            print('nav deriga atzime')
d=sekmjuizraksts()
d.atzime(6)
d.atzime(9)
d.atzime(10)
print(d.sekmes)



