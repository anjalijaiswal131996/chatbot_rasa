import requests
import json

def getdistrict(pincode):

    url="https://api.postalpincode.in/pincode/" +str(pincode)
    response = requests.get(url=url)
    response.raise_for_status()
    result=response.json()
    print(result)

    district=result[0]["PostOffice"][0]["District"]
    state=result[0]["PostOffice"][0]["State"]
    return (district ,state )

def getcoviddetails(district,state):

    url="https://api.covid19india.org/state_district_wise.json"
    response = requests.get(url=url)
    response.raise_for_status()
    result=response.json()
    print(result)

    confirmed=result[state]["districtData"][district]["confirmed"]
    active = result[state]["districtData"][district]["active"]
    recovered = result[state]["districtData"][district]["recovered"]
    return (confirmed,active ,recovered )


if __name__=="__main__":

    result=getdistrict(276001)
    print(result)
    covid_details= getcoviddetails(result[0],result[1])
    print(covid_details)
