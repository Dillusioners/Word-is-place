#Author - Dynamax
#Team - Dillusioners
#Word - Place
#Info - Console place info giver

import requests
code = int(input('Enter any postal code to get its place:- '))
try:
    # Adding the postal code to the API Key.
    KEY = 'https://app.zipcodebase.com/api/v1/search?apikey=fa691540-8a5d-11ed-a5b6-21d75d715c14&codes=' + str(code)
    response = requests.get(KEY)
    data = response.json()
    # Getting the data
    city = data['results'][str(code)][0]['city']
    state = data['results'][str(code)][0]['state']
    province = data['results'][str(code)][0]['province']
    country_code = data['results'][str(code)][0]['country_code']
    
    # Printing the data
    print("---------------")
    print("****RESULTS****")
    print("--------------")
    print("City: ", city)
    print("State: ", state)
    print("Province: ", province)
    print("Country: ", country_code)
    print("---------------")
except:
    print("---------------")
    print("Ran into an error.")
    print("---------------")