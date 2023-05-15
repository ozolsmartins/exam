import requests
response=requests.get("http://universities.hipolabs.com/search?country=Canada")
schools=response.json()
for school in schools:
    print(school["name"])

def sortParamater(e):
    return e["name"]
schools.sort(key=sortParamater)
for school in schools:
    if school["domains"][0]=="scar.utoronto.ca":
        print(school["name"])