import requests

url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

city=input("city: ")
querystring = {"q":city,"days":"3"}

headers = {

    "X-RapidAPI-Key": "d715e91b9dmshead6b2171984ec6p105b4fjsn2391809a102f",

    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"

}

response = requests.request("GET", url, headers=headers, params=querystring)

res=response.json()
print(res["forecast"]["forecastday"][0])



for i in range(3):
    print(res["forecast"]["forecastday"][i]["date"], res["forecast"]["forecastday"][i]["day"]["condition"]["text"], "and", res["forecast"]["forecastday"][i]["day"]["avgtemp_c"], "°C")