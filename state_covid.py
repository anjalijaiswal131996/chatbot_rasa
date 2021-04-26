import requests
import json


def getcoviddetaistate(state):

    url="https://api.covid19india.org/data.json"
    response = requests.get(url=url)
    response.raise_for_status()
    result=response.json()
    print(result)
    confirmed=0
    active=0
    recovered=0
    result = result["statewise"]
    for k in result:
        if k["state"] == state:
            confirmed = k["confirmed"]
            active = k["active"]
            recovered = k["recovered"]
    return (confirmed,active ,recovered )



if __name__=="__main__":


    covid_detail= getcoviddetaistate("Delhi")
    print(covid_detail)
