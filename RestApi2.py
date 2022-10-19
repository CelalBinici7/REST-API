import requests

URL = "https://www.freetogame.com/api/games"

response = requests.get(URL)

print(response.text)