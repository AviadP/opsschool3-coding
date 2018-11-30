import click
from weather import Weather, Unit


TODAY_FORECAST_LENGTH = 1
MAX_FORECAST_LENGTH = 9


def get_weather_info_by_city(city, units):
    if units == "-c":
        weather = Weather(unit=Unit.CELSIUS)
        selected_units = "Celsius"
        city_weather_info = weather.lookup_by_location(city)
        forecasts = city_weather_info.forecast

        return forecasts, selected_units

    elif units == "-f":
        weather = Weather(unit=Unit.FAHRENHEIT)
        selected_units = "Fahrenheit"
        city_weather_info = weather.lookup_by_location(city)
        forecasts = city_weather_info.forecast

        return forecasts, selected_units

    else:
        print("none or wrong units selected")
        exit(1)


def get_forecast_length(forecast):
    split_forecast = forecast.split("+")
    if len(split_forecast) == TODAY_FORECAST_LENGTH:
        forecast_length = 0
    else:
        forecast_length = int(split_forecast[1])

    if forecast_length > MAX_FORECAST_LENGTH:
        print("Required forecast in unknown, forecast of up to 10 days may be displayed")
        exit(1)

    return forecast_length


def print_output(city, units, forecasts, forecast_length):
    if forecast_length == 0:
        condition = forecasts[0].text
        high = forecasts[0].high
        low = forecasts[0].low
        output_string = "The weather in {city} today is {condition} with temperatures trailing from ({low})-({high}) " \
                        "{units}".format(city=city, condition=condition, high=high, low=low, units=units)
        print(output_string)
        return 0
    else:
        for day in range(0, forecast_length + 1):
            date = forecasts[day].date
            condition = forecasts[day].text
            high = forecasts[day].high
            low = forecasts[day].low
            output_string = "{date} {condition} with temperatures trailing from ({low})-({high}) {units}".format(
                date=date,
                city=city, condition=condition, high=high, low=low, units=units)
            print(output_string)
        return 0


@click.command()
@click.option("--city", help="selected city")
@click.option('-c', 'units', required=True, flag_value='-c', type=str, help='Display temperature in Celsius.')
@click.option('-f', 'units', required=True, flag_value='-f', type=str, help='Display temperature in Fahrenheit.')
@click.option("--forecast", required=False, default="TODAY", show_default=True,
              help="selected days , starting from today"
                   "for example: --forecast TODAY for today's forecast, TODAY+3 for next 3 days")
def main(city, units, forecast):
    forecasts, units = get_weather_info_by_city(city, units)
    forecast_length = get_forecast_length(forecast)
    print_output(city, units, forecasts, forecast_length)


if __name__ == "__main__":
    main()
