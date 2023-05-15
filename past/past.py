f=open("pasts.txt")
gar=len(f.read())
f.seek(0)
vards=""
vietas=[]
for i in range(gar):
    c=f.read(1)
    if c==" ":
        if len(vietas)==0:
            vietas.append(vards)
        else:
            index=0
            for i in range(len(vietas)):
                if vards[0]>vietas[i][0]:
                    index+=1
            vietas.insert(index,vards)
        vards=""
    else:
        vards+=c
print(vietas)