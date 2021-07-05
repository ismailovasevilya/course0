import request
import json

api_url = "http://numbersapi.com/#42"

number = int(input())

params = {
    'number' : number
}

res = requests.get(api_url, params=params)

data = res.json

if data.found == False:
    print("Boring")
else:
    print("Interesting")

