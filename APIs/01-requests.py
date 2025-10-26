import requests

EndPoint = "https://api.openweathermap.org/data/2.5/onecall"
# EndPoint = "https://api.openweathermap.org/data/3.0/onecall"

# EndPoint = "https://api.openweathermap.org/data/2.5/weather"            # current weather data.

api_key = "2f8c67112de82db3d84d33dd2ac9168b"
# api_key = "869ede5ba77b118a47156e0dba091ae4"

wat_params = {
    'lat' : 51.507351, 
    'lon' : -0.127758,
    'appid' : api_key,
}


response = requests.get(EndPoint, params=wat_params)
print(response.status_code)

data = response.json()
print(data)