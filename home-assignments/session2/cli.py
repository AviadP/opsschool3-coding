from weather import Weather, Unit
import click


def draft():
    temp_units = input("select required temperature units, type 1 for celsius, 2 for Fahrenheit ")
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

    announcement = "the temperature in {0} today is {1} with temperature trailing from {2}-{3} {4}".format(city,
                                                                                                           condition,
                                                                                                           high, low,
                                                                                                           selected_units)

    print(announcement)


def get_weather_info_by_city(city):
    weather = Weather(unit=Unit.CELSIUS)

    city_weather_info = weather.lookup_by_location(city)

    return city_weather_info


def forecast_by_weather_info(city_weather_info):
    forecasts = city_weather_info.forecast
    condition = []
    high = []
    low = []
    for forecast in forecasts:
        condition.append(forecast.text)
        high.append(forecast.high)
        low.append(forecast.low)

    full_forecast_info = {"condition": condition, "high": high, "low": low}
    print(full_forecast_info)

    return full_forecast_info





@click.command()
@click.option("--city", help="selected city")
@click.option("--forecast", help="selected days , starting from today"
                                 "for example: --forecast TODAY for today's forecast, TODAY+3 for next 3 days(including today)")
def main(data):
    pass


city_info = get_weather_info_by_city("Tel Aviv")
print(forecast_by_weather_info(city_info))
