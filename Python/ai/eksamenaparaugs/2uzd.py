with open("text.txt", "r") as f:
    text=f.read()
    print(text)
    nevajadzigi=".,!?:;()"
    for simb in nevajadzigi:
        text=text.replace(simb,"")
    text=text.split(" ")
    print(text)

    vardu_skaits={} #key->value
    for vards in text:
        if len(vards)>3:
            #vardu skaits key=vards, value=text.count(vards)
            vardu_skaits[vards]=text.count(vards)
    sakartots=sorted(vardu_skaits,key=vardu_skaits.get)
    for i in sakartots:
        print (i," ",vardu_skaits[vards])
