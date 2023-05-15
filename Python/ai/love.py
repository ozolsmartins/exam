import requests

url = "https://love-calculator.p.rapidapi.com/getPercentage"

querystring = {"sname":"Mārtiņš","fname":"Keratina"}

headers = {
	"X-RapidAPI-Key": "0b73437c2bmsh4ecc30ef11ff701p1a3afcjsn179baf7d5939",
	"X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)