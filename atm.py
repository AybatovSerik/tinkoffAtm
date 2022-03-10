# coding: utf-8
from typing import List
import json

class ATM:
    def __init__(self, id: str, location: str, usd: float, eur: float, rub: float):
        self.id = id
        self.location = location
        self.usd = usd
        self.eur = eur
        self.rub = rub

    def __str__(self):
        return f"{self.id}: usd -> {self.usd}, eur -> {self.eur}, rub -> {self.rub} : {self.location}"

    def __eq__(self, new):
        if (self.usd == new.usd) & (self.rub == new.rub) & (self.eur == new.eur):
            return True
        else:
            return False


def parseATM_fromJsonPoint(point):
    location = point["address"]
    id = point["id"]
    limits = point["atmInfo"]["limits"]
    rub = -1
    usd = -1
    eur = -1
    for curr in limits:
        if curr["currency"] == "RUB":
            rub = float(curr["amount"])
        if curr["currency"] == "USD":
            usd = float(curr["amount"])
        if curr["currency"] == "EUR":
            eur = float(curr["amount"])

    return ATM(id, location, usd, eur, rub)



def parseATM(json_file):
    atms = []

    with open(json_file,"r", encoding="utf-8") as f:
        jsoned = json.load(f)

    clusters = jsoned["payload"]["clusters"]
    for cluster in clusters:
        # print(len(cluster["points"]))
        # print(cluster["points"])
        points = cluster["points"]
        for point in points:
            # print(point["atmInfo"]["limits"])
            atm = parseATM_fromJsonPoint(point)
            atms.append(atm)

    return atms


# parseATM("json_example.txt")