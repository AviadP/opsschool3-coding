import requests


"""
location_by_ip_api = 'http://ip-api.com/json'

weather_api = 'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&APPID=07de467d22717f0eeee1c32550a7ebb1
"""
url = "http://ip-api.com/json"
my_location = requests.get(url=url)
my_location =my_location.json()
#print(my_location)

my_city = my_location['city']
my_country = my_location['country']

#print("{0} ,{1}".format(my_city, my_country))

weather_url = "http://api.openweathermap.org/data/2.5/weather?q={city},{country}&units=metric&APPID=07de467d22717f0eeee1c32550a7ebb1".format(city=my_city, country=my_country)
weather = requests.get(url=weather_url)
weather = weather.json()

print(weather)