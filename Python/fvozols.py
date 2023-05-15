class Paralelskaldnis:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def tilpums(self):
        return self.a*self.b*self.c
    def v_S(self):
        return 2*(self.a*self.b)+2*(self.a*self.c)+2*(self.b*self.c)
    def diognale(self):
        return (((self.a**2)+(self.b**2))+self.c**2)**0.5
paralel=Paralelskaldnis(3,4,6)
print(paralel.tilpums())
print(paralel.v_S())
print(paralel.diognale())