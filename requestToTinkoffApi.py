import requests

requestJson = '''{"bounds":{"bottomLeft":{"lat":55.82318429323392,"lng":37.44886437488061},"topRight":{"lat":55.858054050945746,"lng":37.552891169314194}},"filters":{"banks":["tcs"],"showUnavailable":true,"currencies":["RUB"]},"zoom":14}'''
headers = {"content-type" : "application/json"}

def makeRequest():
    requestResponse = requests.post("https://api.tinkoff.ru/geo/withdraw/clusters", data=requestJson, headers=headers)
    with open("requestResponse.txt","w", encoding="utf-8") as f:
        f.write(requestResponse.text)