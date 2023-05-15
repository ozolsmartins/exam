# Klase MyPoint, kas implementē sekojošo:
# konstruktors, kur tiek padots punkta x un y
# Funkcijas setX, setY, getXY, moveRight(d), moveLeft(d),
# moveUp(d), moveDown(d), distanceTo(point)
# Nodrošināt funkcionalitāti tā, lai punktu nebūtu iespējams
# pārvietot tālāk par 100 vienībām uz jebkuru pusi no
# _sākotnējās_ pozīcijas
# izveidot MyPoint objektu, nodemonstrēt vismaz četru
# iekšējo funkciju darbību

# Klase Circle, kas par centra punktu izmanto MyPoint klases objektu
# implementē visas funkcijas, kas raksturīgas riņķa līnijai
# konstruktorā MyPoint objekts un rādiuss

class MyPoint:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.limits=[self.y+100, self.x+100, self.y-100, self.x-100]
    def setX(self,x):
        self.x=x
    def setY(self,y):
        self.y=y
    def getXY(self):
        return [self.x,self.y]
    def moveRight(self,d):
        if self.x+d>self.limits[1]:
            print("overflow")
        else:
            self.x=self.x+d
        
    def moveLeft(self,d):
        if self.x+d>self.limits[3]:
            print("overflow")
        else:
            self.x=self.x+d
        
    def moveUp(self,d):
        if self.x+d>self.limits[0]:
            print("overflow")
        else:
            self.yx=self.y+d
        
    def moveDown(self,d):
        if self.x+d>self.limits[2]:
            print("overflow")
        else:
            self.y=self.y-d
        
    def distanceTo(self, point):
        xd=self.x-point.x
        yd=self.y-point.y
        return ((xd)**2+(yd)**2)**0.5
p1=MyPoint(2,4)
p2=MyPoint(5,7)
print(p1.distanceTo(p2))
p1.moveUp(101)
p1.moveRight(5)
p1.moveDown(2)
print(p1.getXY())

class Circle:
    def __init__(self,c,r):
        self.c=c
        self.r=r
    def laukums(self):
        return 3.14*(self.r**2)
    def perimetrs(self):
        return 2*3.14*self.r
    def overlap(self,circle):
        if circle.c.distanceTo(self.c)>circle.r+self.r:
            return False
        else:
            return True
p3=MyPoint(1,3)
p4=MyPoint(40,70)
aplis1=Circle(p3,8)
aplis2=Circle(p4,10)
print(aplis1.laukums())
print(aplis1.perimetrs())
print(aplis1.overlap(aplis2))

    
    