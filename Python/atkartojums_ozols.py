##summa=0
##skaitlis=int(input("ievadi skaitli"))
##while skaitlis!=0:
##    summa+=skaitlis
##    skaitlis=int(input("ievadi skaitli"))
##print(summa)
##
##
##sum=0
##x=int(input("ievadi skaitli"))
##if x>99 and x<1000:
##    vieni=x%10
##    desmiti=((x-vieni)%100)/10
##    simti=(x-vieni-(desmiti*10))%1000/100
##    sum=vieni+desmiti+simti
##else:
##    print("kluda, nav trisciparu skaitlis")
##print(sum)
##
##def vektora_garums(x,y):
##    garums=(x**2+y**2)**0.5
##    return garums
##print(vektora_garums(1,2))

##class datums:
##    def __init__(self,d,m):
##        if d<1 or d>31:
##            print("datums nav pareizs")
##            self.diena=1
##        else:
##            self.diena=d
##        if m<1 or m>12:
##            print("menesis nav pareizs")
##            self.menesis=1
##        else:
##            self.menesis=m
##    def printdatums(self):
##        return str(self.diena)+" "+str(self.menesis)
##    def nakosadiena(self):
##        self.diena+=1
##a=datums(16,3)
##print(a.printdatums())
##a.nakosadiena()
##print(a.printdatums())
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
        return str(self.sekundes)+":"+str(self.minutes)
a=laiks(3,58)
a.printlaiks()
a.nakosasekunde()
a.printlaiks()
a.nakosasekunde()
a.printlaiks()