import requests
import json
import time

print('From LL (xenium) as a joke')


print('repeats of algo')
repeats = int(input())

url = "https://api.hamsterkombatgame.io/clicker/tap"

#Import your authorization header from POST request in borwser
auth = ''
print("your energy capacity:")
batt = int(input())
interval = int(batt/3)

for x in range(repeats):
    tstmp = int(time.time())
    data = {"count":batt,"availableTaps":0,"timestamp":tstmp}
    headers = {'Host': 'api.hamsterkombatgame.io', "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0','Accept': 'application/json','Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3','Accept-Encoding': 'gzip, deflate, br','Referer': 'https://hamsterkombatgame.io/','authorization': auth,'content-type': 'application/json','Content-Length': '55','Origin': 'https://hamsterkombatgame.io','Connection': 'keep-alive','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','TE': 'trailers'}
    requests.post(url, json=data, headers=headers)
    time.sleep(interval)

