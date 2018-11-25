import requests
import json


def check_self_location_by_ip():
    ip_api_url = "http://ip-api.com/json"
    try:
        my_location = requests.get(url=ip_api_url)
        my_location = my_location.json()
    except Exception as e:
        print(e)
        exit(1)
    my_city = my_location['city']
    my_country = my_location['country']
    location = (my_city, my_country)

    return location


def get_weather_by_location(location):
    city = location[0]
    country = location[1]
    try:
        weather_url = "http://api.openweathermap.org/data/2.5/weather?q={city}," \
                      "{country}&units=metric&APPID=07de467d22717f0eeee1c32550a7ebb1".format(
            city=city, country=country)
        weather = requests.get(url=weather_url)
        weather = weather.json()
    except Exception as e:
        print(e)
        exit(0)

    return weather


def write_to_file(data, file_name):
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(json.dumps(data))
    except Exception as e:
        print(e)
        exit(1)


def parse_temp_from_weather(weather):
    temp = weather["main"]["temp"]
    name = weather["name"]
    temp_w_name = (temp, name)

    return temp_w_name


def display_multiple_cities_weather(cities_list: list):
    for place in cities_list:
        weather = get_weather_by_location(place)
        temp_w_name = parse_temp_from_weather(weather)
        if temp_w_name[1] == place[0]:
            line = "The weather in {city}, {country} is {temp} degrees\n".format(city=place[0], country=place[1],
                                                                                 temp=temp_w_name[0])
            print(line)
        else:
            print("{city} name is not correct\n".format(city=place[0]))


def main():
    cities_list = [("Tel Aviv", "Israel"), ("Haifa", "Israel"), ("Jerusalem", "Israel"), ("Rehovot", "Israel"),
                   ("Beer Sheva", "Israel"), ("London", "England"), ("Helsinki", "Finland"), ("Munich", "Germany"),
                   ("Paris", "French"), ("Frankfurt", "Germany")]
    location = check_self_location_by_ip()
    weather = get_weather_by_location(location)
    parse_temp_from_weather(weather)
    display_multiple_cities_weather(cities_list)
    write_to_file(weather, "weather.txt")


if __name__ == "__main__":
    main()
