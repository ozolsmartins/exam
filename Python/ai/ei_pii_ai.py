import requests

# response=requests.get("https://catfact.ninja/fact")
# catFact=response.json()
# print(catFact["fact"])
name=input("IEVADI. VĀRDU.")

while name !="":
    response=requests.get("https://api.genderize.io?name="+name)
    res=response.json()
    print(res)
    # print(name, "DZĪVOS. VĒL.", age, "gadu vecumam")
    name=input("IEVADI. VĀRDU.")
