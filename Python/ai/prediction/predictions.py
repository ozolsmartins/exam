import requests

url = "https://football-prediction-api.p.rapidapi.com/api/v2/predictions"

querystring = {"market":"classic","iso_date":"2018-12-01","federation":"UEFA"}

headers = {
	"X-RapidAPI-Key": "0b73437c2bmsh4ecc30ef11ff701p1a3afcjsn179baf7d5939",
	"X-RapidAPI-Host": "football-prediction-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)


for game in response.json()["data"]:
    print(game["home_team"],"vs",game["away_team"],game["prediction"])