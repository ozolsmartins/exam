skaitli={
    "00":" ",
    "01":"pirmais",
    "02":"otrais",
    "03":"tresais",
    "04":"ceturtais",
    "05":"piektais",
    "06":"sestais",
    "07":"septitais",
    "08":"astotais",
    "09":"devitais",
    "10":"desmitais",
    "11":"vienpadsmitais",
    "12":"divpadsmitais",
    "13":"trispadsmitais",
    "14":"cetrpadsmitais",
    "15":"piecpadsmitais",
    "16":"sespadsmitais",
    "17":"septinpadsmitais",
    "18":"astonpadsmitais",
    "19":"devinpadsmitais",

}
desmiti={
    "1":"desmit",
    "2":"divdesmit",
    "3":"trisdesmit"
}
menesi={
    "01":"janvaris",
    "02":"februaris",
    "03":"marts",
    "04":"aprilis",
    "05":"maijs",
    "06":"junijs",
    "07":"julijs",
    "08":"augusts",
    "09":"septembris",
    "10":"oktobris",
    "11":"novembris",
    "12":"decembris"
}
datums=input("ievadi datumu DD.MM")
datumsplit=datums.split(".")
datumsplitsplit=datumsplit[0].split
if int(datumsplit[1])==2:
    if int(datumsplitsplit[0])<=2 and int(datumsplitsplit[1])<=8:
        if int(datumsplitsplit[1])==0:
            print(desmiti[datumsplitsplit[0]]+str("ais"),menesi[datumsplit[1]])
        elif int(datumsplitsplit[1])>0:
            print(desmiti[datumsplitsplit[0]],skaitli[datumsplitsplit[1]], menesi[datumsplit[1]])
    else:
        countdown_time=10
        while countdown_time>=0:
            print(countdown_time)
            countdown_time-=1
        print("Self-destruct sequence initiated")
elif int(datumsplit[1])==4 or int(datumsplit[1])==6 or int(datumsplit[1])==9 or int(datumsplit[1])==11:
    if (int(datumsplitsplit[0])<=3 and int(datumsplitsplit[1])==0) or (int(datumsplitsplit[0])<=2 and int(datumsplitsplit[1])<=9):
        if int(datumsplitsplit[1])==0:
            print(desmiti[datumsplitsplit[0]]+str("ais"),menesi[datumsplit[1]])
        elif int(datumsplitsplit[1])>0:
            print(desmiti[datumsplitsplit[0]],skaitli[datumsplitsplit[1]], menesi[datumsplit[1]])
    else:
        print("Fatal Python error: init_import_size: Failed to import the site module Python runtime state: initialized")
elif int(datumsplit[1])==1 or int(datumsplit[1])==3 or int(datumsplit[1])==5 or int(datumsplit[1])==7 or int(datumsplit[1])==8 or int(datumsplit[1])==10 or int(datumsplit[1])==12:
    if (int(datumsplitsplit[0])<=3 and int(datumsplitsplit[1])==1) or (int(datumsplitsplit[0])<=2 and int(datumsplitsplit[1])<=9):
        if int(datumsplitsplit[1])==0:
            print(desmiti[datumsplitsplit[0]]+str("ais"),menesi[datumsplit[1]])
        elif int(datumsplitsplit[1])>0:
            print(desmiti[datumsplitsplit[0]],skaitli[datumsplitsplit[1]], menesi[datumsplit[1]])
    else:
        print("Fatal Python error: init_import_size: Failed to import the site module Python runtime state: initialized")
else:
    print("kaut kas nogaja greizi")