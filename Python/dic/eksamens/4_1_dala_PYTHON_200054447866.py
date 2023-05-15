import requests
response=requests.get('http://universities.hipolabs.com/search?country=latvia')
response=response.json()
print(response)
names=[]
for school in response:
    names.append(school["name"])
names.sort()
print(names)
for name in names:
    print(name)
