class Kvadratvienadojums:
    def __init__(self,x, y, z):
        self.a=x
        self.b=y
        self.c=z
    def diskriminants(self):
        return self.b**2-4*self.a*self.c
    def sakne1(self):
        if self.diskriminants()>=0:
            return (-self.b+self.diskriminants()**0.5)/(2*self.a)
        else:
            print("diskriminants negativs")
    def sakne2(self):
        if self.diskriminants()>=0:
            return (-self.b-self.diskriminants()**0.5)/(2*self.a)
        else:
            print("diskriminants ir negativs")
    def xvirsotne(self):
        return -self.b/(2*self.a)
    def yvirsotne(self):
        return self.a*self.xvirsotne()**2+self.b*self.xvirsotne()+self.c
d=Kvadratvienadojums(4,6,2)
print("D=",d.diskriminants())
print("x1=",d.sakne1())
print("x2=",d.sakne2())
print("parabolas virsotne= (",d.xvirsotne(),",",d.yvirsotne(),")")

class Dziesma:
    def __init__(self, nosaukums, izpilditajs, garums, albums):
        self.title=nosaukums
        self.artist=izpilditajs
        self.lenght=garums
        self.album=albums
    def print1(self):
        print(self.artist,"-", self.title)
    def print2(self):
        print(self.title,"-",self.lenght)
    def print3(self):
        print(self.artist,"-",self.album)
muzika=Dziesma("Off The Grid","Kanye West","5:39","Donda")
muzika.print1()
muzika.print2()
muzika.print3()
class datums:
    def __init__(self,d,m):
        if d<1 or d>31:
            print("datums nav pareizs")
            self.diena=1
        else:
            self.diena=d
        if m<1 or m>12:
            print("menesis nav pareizs")
            self.menesis=1
        else:
            self.menesis=m
    def printdatums(self):
        return str(self.diena)+" "+str(self.menesis)
    def nakosadiena(self):
        if self.menesis==2:
            if self.diena==28:
                self.diena=1
                self.menesis+=1
            else:
                self.diena+=1
        elif self.menesis==4 or self.menesis==6 or self.menesis==9 or self.menesis==11:
            if self.diena==30:
                self.diena=1
                self.menesis+=1
            else:
                self.diena+=1
        else:
            if self.diena==31:
                if self.menesis==12:
                    self.diena=1
                    self.menesis=1
                else:
                    self.diena+=1
            else:
                self.diena+=1

a=datums(31,12)
print(a.printdatums())
a.nakosadiena()
print(a.printdatums())

