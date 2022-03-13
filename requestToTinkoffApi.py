import requests


headers = {"content-type" : "application/json"}

def makeRequest():
    requestJson = '''{"bounds":{"bottomLeft":{"lat":55.82318429323392,"lng":37.44886437488061},"topRight":{"lat":55.858054050945746,"lng":37.552891169314194}},"filters":{"banks":["tcs"],"showUnavailable":true,"currencies":["RUB"]},"zoom":14}'''
    requestResponse = requests.post("https://api.tinkoff.ru/geo/withdraw/clusters", data=requestJson, headers=headers)
    with open("requestResponse.txt","w", encoding="utf-8") as f:
        f.write(requestResponse.text)


def makeRequestWork():
    requestJson = '''{"bounds":{"bottomLeft":{"lat":55.795303863006296,"lng":37.499604317770284},"topRight":{"lat":55.81275521736427,"lng":37.551617714987074}},"filters":{"banks":["tcs"],"showUnavailable":true,"currencies":["RUB"]},"zoom":15}'''
    requestResponse = requests.post("https://api.tinkoff.ru/geo/withdraw/clusters", data=requestJson, headers=headers)
    with open("requestResponseWork.txt","w", encoding="utf-8") as f:
        f.write(requestResponse.text)