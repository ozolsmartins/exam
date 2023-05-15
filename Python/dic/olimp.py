#izveidot programmu, kas izveido vārdnīcu garumā 10;
#key vērtības ir naturāli skaitļi 1-10, katram key x pretī ir value x^2

# dic={}
# for i in range(1,11):
#     dic[i]=i**2
# #dots teksta fails 'olimp.txt', kur definēta vārdnīca garumā 6
# #ievaddatu katra rindiņa satur key-value pāri
# #nolasīt ievaddatus, izveidojot vārdnīcu

dic={}
dic2={
    '3':'10',
    '6':'9',
    '9':'0'
}
#faila atvēršana
with open("olimp.txt") as f:
    #readlines izveido masīvu no rindiņām
    lines=f.readlines()
    print(lines)
    #apstrādājam katru rindiņu masīvā
    for line in lines:
        #izdalām rindiņu uz pusēm, izmanto atstarpi
        key_value=line.split()
        print(key_value)
        #iegūtās vērtības izmantojam dictionary izpildē
        dic[key_value[0]]=key_value[1]
for key in dic:
    if dic[key] in dic2:
        print(key, dic2[dic[key]])



with open("olimpdic.txt") as f:
    line1=f.readline()
    vertibas=line1.split()
    print(vertibas)
    pSkaits=int(vertibas[0])
    zPieturas=int(vertibas[1])
    posmi=int(vertibas[2])
    print(pSkaits,zPieturas, posmi)
    pieturas={i:[] for i in range(1,12)}
    for _ in range(posmi):
        #nolasām vienu rindu
        line=f.readline()
        #sadalām rindinu pa atstarpēm, lai iegutu atseviski katru vērtību rindā
        line=line.split()
        #iegūstam katras vērtības skaitlisko vērtību
        line[0]=int(line[0])
        line[1]=int(line[1])
        
        pieturas[line[0]].append(line[1])
        pieturas[line[1]].append(line[0])
    zalas={}
    sarkanas={}
    for key in pieturas:
        if key>7:
            sarkanas[key]=pieturas[key]
        else:
            zalas[key]=pieturas[key]
    print(zalas, sarkanas)
        
        
    