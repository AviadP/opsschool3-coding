from weather import Weather, Unit

def draft():

    temp_units = input("select required temperture units, type 1 for celsius, 2 for Fahrenheit ")
    if temp_units == "1":
        weather = Weather(unit=Unit.CELSIUS)
        selected_units = "CELSIUS"
    elif temp_units == "2":
        weather = Weather(unit=Unit.FAHRENHEIT)
        selected_units = "FAHRENHEIT"
    else:
        print("wrong input")
        exit(1)

    city = 'oslo'
    city_weather_info = weather.lookup_by_location(city)

    condition = city_weather_info.forecast[0].text
    high = city_weather_info.forecast[0].high
    low = city_weather_info.forecast[0].low

    announcement = "the temperture in {0} today is {1} with temperture trailing from {2}-{3} {4}".format(city, condition,
                                                                                                         high, low,
                                                                                                         selected_units)

    print(announcement)
