class TaisnlenkaTrijsturis:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def perimetrs(self):
        return self.a+self.b+((self.a**2+self.b**2)**0.5)
    def laukums(self):
        return (self.a*self.b)/2


class Trapece:
    def __init__(self,a,b,h):
        self.a=a
        self.b=b
        self.h=h
    def viduslinija(self):
        return (self.a+self.b)/2
    def laukums(self):
        return ((self.a+self.b)/2)*self.h
trapece=Trapece(3,4,6)

class ToDoList:
    def __init__(self,x):
        self.x=x
    def check(self):
        if self.x==0:
            print("all done")
        else:
            self.x-=1
            return self.x

class Stunda:
    def __init__(self,h):
        self.h=h
    def add(self,x):
        self.h=self.h+x
        if self.h>24:
            self.h-=24
            return self.h
        else:
            return self.h


stunda=Stunda(24)
print(stunda.add(5))
print(stunda.add(26))

        