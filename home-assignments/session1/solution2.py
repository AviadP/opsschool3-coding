import requests
import json


def draft():
    """
    location_by_ip_api = 'http://ip-api.com/json'

    weather_api = 'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&APPID=07de467d22717f0eeee1c32550a7ebb1
    """
    url = "http://ip-api.com/json"
    my_location = requests.get(url=url)
    my_location = my_location.json()
    # print(my_location)

    my_city = my_location['city']
    my_country = my_location['country']

    # print("{0} ,{1}".format(my_city, my_country))

    weather_url = "http://api.openweathermap.org/data/2.5/weather?q={city},{country}&units=metric&APPID=07de467d22717f0eeee1c32550a7ebb1".format(
        city=my_city, country=my_country)
    weather = requests.get(url=weather_url)
    weather = weather.json()

    print(weather)


def check_self_location_by_ip():
    ip_api_url = "http://ip-api.com/json"
    my_location = requests.get(url=ip_api_url)
    my_location = my_location.json()
    my_city = my_location['city']
    my_country = my_location['country']
    location = (my_city, my_country)

    return location


def get_weather_by_location(location):
    city = location[0]
    country = location[1]
    weather_url = "http://api.openweathermap.org/data/2.5/weather?q={city},{country}&units=metric&APPID=07de467d22717f0eeee1c32550a7ebb1".format(
        city=city, country=country)
    weather = requests.get(url=weather_url)
    weather = weather.json()

    return weather


def write_to_file(data, file_name):
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(json.dumps(data))
        exit(0)


def main():
    location = check_self_location_by_ip()
    weather = get_weather_by_location(location)
    write_to_file(weather, "weather.txt")


if __name__ == "__main__":
    main()
