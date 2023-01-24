import requests
import json 
URL = "https://www.freetogame.com/api/games"

result = requests.get(URL)
response = json.loads(result.text)[3]

name = response["title"]
genre = response["genre"]
platform = response["platform"]
developer = response["developer"]

print(f"{name}")
print(f"genre :{genre}")
print(f"platform : {platform}")
print(f"developer : {developer}")
