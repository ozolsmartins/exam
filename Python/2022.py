# x=int(input("ievadi skaitli"))
# if x>10:
#     print("skaitlis lielaks par 10")
# elif x==10:
#     print("daunis")
# else:
#     print("ne")


# x=int(input("ievadi skaitli"))
# while x!=0:
#     x=int(input("ievadi skaitli"))

# for i in range(1,21):
#     if i%2!=0:
#         print(i)

# m=[1,4,2,7,3]
# for i in range(len(m)):
#     print(m[i])

# dd={[1,4,2,7,3],
#     [1,4,2,7,3],
#     [1,4,2,7,3],
#     [1,4,2,6,3],
#     [1,4,2,7,3]}
# print(dd[3][3])

# teikums="yoyoyo bois"
# print(len(teikums))
# print(teikums.count(" ")+1) 
# vardi=teikums.split(" ")
# print(len(vardi))
# jauns=[]
# for vards in vardi:
#     if len(vards)>0:
#         jauns.append(vards)
# print(jauns)

# text="TukumaRainaValstsGimnazija"
# for char in text:
#     if ord(char)>64 and ord(char)<91:
#         print(" ", end="")
#         print(char, end="")
#     else:
#         print(char,end="")
# text="tukuma raina valsts gimnazija"
# c=chr(ord(text[0])-32)
# i=0
# temp=0
# x=""
# while i<len(text):
#     if i==temp:
#         x+=chr(ord(text[i])-32)
#     elif text[i]==" ":
#         temp=i+1
#         x+=" "
#     else:
#         x+=text[i]
#     i+=1
    
# print(x)

# def summa(n):
#     x=0
#     while n>0:
#         sk=n%10
#         n=(n-sk)//10
#         x+=sk
#     return x
# print(summa(123))
        

# def apgr(n):
#     x=0
#     while n>0:
#         sk=n%10
#         n=(n-sk)//10
#         x=x*10+sk
#     return x
# print(apgr(325))       
# def mas(n):
#     mas=[]
#     i=0
#     while n>0:
#         sk=n%10
#         n=(n-sk)//10
#         mas.insert(0,sk)
#     return mas

    
# print(mas(123))

# def para(masiv):
#     i=0
#     for elem in masiv:
#         if elem%2==0:
#             i+=1
#     return i
# print(para([1,2,3,4,5,6,7]))

# def augos(masiiv):
#     for i in range(len(masiiv)-1):
#         if masiiv[i]>masiiv[i+1]:
#             return False

#     return True
    
# print(augos([1,2,1,3]))
# def lielakais(x):
#     lielakais=x[0]
#     for i in range(len(x)):
#         if x[i]>lielakais:
#             lielakais=x[i]
#     return lielakais
# print(lielakais([1,2,3,4,5,6]))   

# m=[3,6,1,2,8,3]
# while not augos(m):
#     for i in range(len(m)-1):
#         if m[i]>m[i+1]:
#             temp=m[i]
#             m[i]=m[i+1]
#             m[i+1]=temp
# print(m)

# class Person:
#     def __init__(self,name, surname):
#         self.name=name
#         self.surname=surname
#     def fullname(self):
#         return self.name+" "+self.surname
# atis=Person("Atis","Ozols")

# class Student(Person):
#     apNr="ao1234"
# atis=Student("Atis","Ozols")
# print(atis.fullname())



# class Circle:
#     def __init__(self, radius, color="white"):
#         self.radius=radius
#         self.color=color
#     def getRadius(self):
#         return self.radius
#     def setRadius(self,r):
#         self.radius=r
#     def getArea(self):
#         return self.radius**2*3.14
#     def getCircumference(self):
#         return 2*self.radius*3.14
#     def getColor(self):
#         return self.color
#     def setColor(self,c):
#         self.color=c
#     def toString(self):
#         return str(self.getRadius())+" "+str(self.getCircumference())+" "+str(self.getArea())+" "+str(self.getColor())

# circle1=Circle(4)
# print(circle1.setRadius(5))
# print(circle1.getRadius())
# print(circle1.toString())




# class Employee:
#     def __init__(self, firstName,lastName, salary):
#         self.name=firstName
#         self.surname=lastName
#         self.salary=salary
#     def getFirstName(self):
#         return self.name
#     def getLastName(self):
#         return self.surname
#     def getName(self):
#         return self.surname+" "+ self.name
#     def getSalary(self):
#         return self.salary
#     def setSalary(self,s):
#         self.salary=s
#     def getAnnualSalary(self):
#         return self.salary*12
#     def raiseSalary(self,proc):
#         self.salary=self.salary*((proc/100)+1)
#     def toString(self):
#         return str(self.getName())+" "+str(self.getAnnualSalary())
# steve=Employee("Steve","Harrington",750)
# print(steve.toString())
# steve.raiseSalary(25)
# print(steve.toString())


# class InvoiceItem:
#     def __init__(self,id,price,qty=1):
#         self.id=id
#         self.price=price
#         self.qty=qty
#     def getId(self):
#         return self.id
#     def getPrice(self):
#         return self.price
#     def setQty(self,q):
#         self.qty=q
#     def getQty(self):
#         return self.qty
#     def getFullPrice(self):
#         return self.price*self.qty
#     def toString(self):
#         return str(self.getId())+" "+str(self.getQty())+" "+str(self.getFullPrice())
# apple=InvoiceItem(1,0.25)
# print(apple.toString())   
# apple.setQty(4)
# print(apple.toString())
# 

# class BankAccount:
#     def __init__(self, id, name, balance=0):
#         self.id=id
#         self.name=name
#         self.balance=balance
#     def getID(self):
#         return self.id
#     def getName(self):
#         return self.name
#     def getBalance(self):
#         return self.balance
#     def credit(self,amount):
#         self.balance+=amount
#     def transferTo(self, account, amount):
#         if amount<=self.getBalance() and self.getID()!=account.getID():
#             self.balance-=amount
#             account.credit(amount)
#         else:
#             print("account",self.getID(),"has insufficient funds and/or IDs are matching", sep=" ")

# account1=BankAccount(19, "Carl Jon", 998765)
# account2=BankAccount(22, "Fanaats Gibala", 321)
# print(account1.getBalance())
# print(account2.getBalance())
# account1.transferTo(account2, 145765)

# print(account2.getBalance())
# print(account1.getBalance())

# from calendar import isleap


# def isLeapYear(year):
#     if year%4==0:
#         if year%100==0:
#             if year%400==0:
#                 return True
#             else:
#                 return False
#         else:
#             return False
#     else:
#         return False
# class Date:
#     def __init__(self, d,m,y):
#         if [4,6,9,11].count(m):
#             if d>0 and d<31:
#                 self.d=d
#                 self.m=m
#                 self.y=y
#             else:
#                 print("invalid input")
#                 self.d=1
#                 self.m=m
#                 self.y=y
        
#         elif m==2:
#             if isLeapYear(y) and d>0 and d<30:
#                 self.d=d
#                 self.m=m
#                 self.y=y
#             elif (not isLeapYear) and d>0 and d<29:
#                 self.d=d
#                 self.m=m
#                 self.y=y
#             else:
#                 print("invalid input")
#                 self.d=1
#                 self.m=m
#                 self.y=y
#         else:
#             if d>0 and d<32 and [1,3,5,7,8,10,12].count(m):
#                 self.d=d
#                 self.m=m
#                 self.y=y
#             else:
#                 print("invalid input")
#                 self.d=1
#                 self.m=m
#                 self.y=y
# def formatsingledigit(d):
#     if d<10:
#         return "0"+str(d)
#     else:
#         return str(d)
# class time:

#     def __init__(self, hh, mm, ss):
#         if hh >= 0 and hh < 24: 
#             self.hh = hh
#         else:
#             print("invalid hour value")
#             self.hh = 0

#         if mm >= 0 and mm < 60: 
#             self.mm = mm
#         else:
#             print("invalid minute value")
#             self.mm = 0

#         if ss >= 0 and ss < 60: 
#             self.ss = ss
#         else:
#             print("invalid second value")
#             self.ss = 0


#     def tostring(self):
#         return formatsingledigit(self.hh) + ":" + formatsingledigit(self.mm) + ":" + formatsingledigit(self.ss)

#     def addtime(self, time):
#         seconds =  self.ss + time.ss
#         minutes = self.mm + time.mm
#         hours = self.hh + time.hh


#         if seconds > 59:
#             minutes += 1
#             seconds = seconds % 60
#         if minutes > 59:
#             hours += 1
#             minutes = minutes % 60
#         if hours > 24:
#             hours = hours % 24
# n = time (2, 44, 25)
# m = time(12, 54, 41)
# m.addtime(n)
# print(m.tostring())
# print(m.tostring())
# def isTaisn(a,b,c):
#             if (a**2)+(b**2)==(c**2) or (a**2)+(c**2)==(b**2) or (c**2)+(b**2)==(a**2):
#                 return True        
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def setX(self,x):
#         self.x=x
#     def setY(self,y):
#         self.y=y
#     def getXY(self):
#         return [self.x,self.y]
#     def distanceTo(self, point):
#         xd=self.x-point.x
#         yd=self.y-point.y
#         return ((xd)**2+(yd)**2)**0.5
# p1=Point(1,4)
# p2=Point(3,8)
# print(p1.distanceTo(p2))

# class Triangle:
#     def __init__(self,p1,p2,p3):
#         self.point1=p1
#         self.point2=p2
#         self.point3=p3
#     def perimeter(self):
#         mala1=self.point1.distanceTo(self.point2)
#         mala2=self.point1.distanceTo(self.point3)
#         mala3=self.point3.distanceTo(self.point2)
#         return sum([mala1,mala2,mala3])
#     def surface(self):
#         mala1=self.point1.distanceTo(self.point2)
#         mala2=self.point1.distanceTo(self.point3)
#         mala3=self.point3.distanceTo(self.point2)
#         p=self.perimeter()/2
#         s=(p*(p-mala1)*(p-mala2)*(p-mala3))**0.5
#         return s


#     def getType(self):
#         a=self.point1.distanceTo(self.point2)
#         b=self.point1.distanceTo(self.point3)
#         c=self.point3.distanceTo(self.point2)
#         if a==b and b==c:
#             return "trijsturis ir rgulars"
#         elif a==b or a==c or b==c:
#             if isTaisn(a,b,c):
#                 return "taisnlenka vienadsanu"
#             else:
#                 return "vienadsanu"
#         else:
#             if isTaisn(a,b,c):
#                 return "taisnlenka dazadmalu"
#             else:
#                 return "dazadmalu"

# t1=Point(1,3)
# t2=Point(3,3)
# t3=Point(3,6)

# tri=Triangle(t1,t2,t3)
# print(tri.perimeter())
# print(tri.surface())
# print(tri.getType())


#inkapsulācija - neļaut piekļūt ārpus klases mainīgajiem
#abstrakcija - neļaut piekļūt iekšējam funkcijām, kas nav būtiskas ārpus klases
#mantošana - izmantot iepriekš minētās vērtības + jaunās
#polimorfisms - līdzīgs mantošanai, bet tā nav tik konkrēta

class Person:
    def __init__(self, vards, uzvards, pk):
        self.vards=vards
        self.uzvards=uzvards
        self.pk=pk
    def FullName(self):
        return str(self.vards+" "+self.uzvards)
p1=Person("Jānis", "Zvirgzdiņš","140404-21131")
print(p1.FullName())
class Teacher(Person):
    def prieksmets(self, prieksmets):
        self.prieksmets=prieksmets
    def dati(self):
        print(self.FullName() +" "+ self.prieksmets)
skolotajs=Teacher("M ", "Ozols", "140404-21131")
skolotajs.prieksmets("programm")
skolotajs.dati()

class Student(Person):
    def klase(self, klase):
        self.klase=klase
    def setIntereses(self):
        interese=input("ievadi interesi:")
        self.intereses=[]
        while len(interese)>0:
            self.intereses.append(interese)
            interese=input("ievadi interesi:")
    def getIntereses(self):
        if self.intereses:
            for interese in self.intereses:
                print(interese)

students=Student("M", "Ozols", "01")
students.setIntereses()
students.getIntereses()
        