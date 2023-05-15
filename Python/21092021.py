class TPrizma:
    def __init__(self,a,b,c,h):
        self.a=a
        self.b=b
        self.c=c
        self.h=h       
    def pam_S(self):
        p=(self.a+self.b+self.c)/2
        return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
    def V(self):
        p=(self.a+self.b+self.c)/2
        return self.h*self.pam_S()
    def SVS(self):
        return (self.a*self.h)+(self.b*self.h)+(self.c*self.h)
    def pilnavirsma(self):
        return 2*self.pam_S()+self.SVS()
prizme=TPrizma(3,4,5,6)
print(prizme.pam_S())
print(prizme.V())
print(prizme.SVS())
print(prizme.pilnavirsma())

