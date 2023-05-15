
vieni={0:'',1:'viens', 2:'divi', 3:'tris', 4:'cetri', 5:'pieci', 6:'sesi', 7:'septini', 8:'astoni', 9:'devini'}
desmiti={0:'',2:'divdesmit', 3:'trisdesmit', 4:'cetrdesmit', 5:'piecdesmit', 6:'sesdesmit', 7:'septindesmit', 8:'astondesmit', 9:'devindesmit'}
padsmiti={0:'desmit',1:'vienpadsmit', 2:'divpadsmit', 3:'trispadsmit', 4:'cetrpadsmit', 5:'piecpadsmit', 6:'sespadsmit', 7:'septinpadsmit', 8:'astonpadsmit', 9:'devinpadsmit'}
simti={0:'',1:'simts', 2:'divi simti', 3:'tris simti', 4:'cetri simti', 5:'pieci simti', 6:'sesi simti', 7:'septini simti', 8:'astoni simti', 9:'devini simti'}

cipars=int(input('ievadi skaitli'))
skaitlis=[]

while cipars>0:
    p=cipars%10
    skaitlis.insert(0,p)
    cipars//=10
while len(skaitlis)<3:
    skaitlis.insert(0,0)
print(skaitlis)

if skaitlis[1]==1:
    print(simti[skaitlis[0]], padsmiti[skaitlis[2]])
else:
    print(simti[skaitlis[0]], desmiti[skaitlis[1]],simti[skaitlis[2]])