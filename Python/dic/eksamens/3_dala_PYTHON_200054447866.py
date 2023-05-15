# class Triangle:
#     def __init__(self,mala1,mala2,mala3):
#         self.mala1=mala1
#         self.mala2=mala2
#         self.mala3=mala3
#     def perimeter(self):
#         if self.mala1+self.mala2>self.mala3 and self.mala1+self.mala3>self.mala2 and self.mala2+self.mala3>self.mala1:
#             return self.mala1+self.mala2+self.mala3, "trijsturis"
#         else:
#             print("error")

# t1=Triangle(4,5,6)
# print(t1.perimeter())

# class Kvadrats:
#     def __init__(self,mala1,mala2,mala3,mala4):
#         self.mala1=mala1
#         self.mala2=mala2
#         self.mala3=mala3
#         self.mala4=mala4
#     def perimeter(self):
#         if self.mala1==self.mala2==self.mala3==self.mala4:
#             return self.mala1+self.mala2+self.mala3+self.mala4, "kvadrats"
#         else:
#             print("error")

# k1=Kvadrats(4,4,4,4)
# print(k1.perimeter())

class Figura:
    def __init__(self,mala1=None,mala2=None,mala3=None,mala4=None):
        self.mala1=mala1
        self.mala2=mala2
        self.mala3=mala3
        self.mala4=mala4
class Perimetrs(Figura):
    def perimeter(self):
        if self.mala1==self.mala2==self.mala3==self.mala4:
            return self.mala1+self.mala2+self.mala3+self.mala4, "kvadrats"
        elif self.mala1==self.mala2 and self.mala3==self.mala4 or self.mala1==self.mala3 and self.mala2==self.mala4 or self.mala1==self.mala4 and self.mala2==self.mala3:
            if self.mala1==self.mala2==self.mala3==self.mala4:
                return self.mala1+self.mala2+self.mala3+self.mala4, "kvadrats"
            else:
                return self.mala1+self.mala2+self.mala3+self.mala4, "taisnsturis"
        elif self.mala1 is None or self.mala2 is None or self.mala3 is None or self.mala4 is None:
            if self.mala1+self.mala2>self.mala3 and self.mala1+self.mala3>self.mala2 and self.mala2+self.mala3>self.mala1:
                return self.mala1+self.mala2+self.mala3, "trijsturis"
            else:
                print("error")
f1=Perimetrs(4,6,4,6)
print(f1.perimeter())
f1=Perimetrs(4,4,4,4)
print(f1.perimeter())
f1=Perimetrs(4,5,6)
print(f1.perimeter())