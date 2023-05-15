import requests
text=input("input text")
text=text.replace(" ","%20")
response=requests.get("https://api.funtranslations.com/translate/yoda.json?text="+text)
yoda=response.json()
print(yoda)
