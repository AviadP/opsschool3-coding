try:
    import click
    from weather import Weather, Unit
except Exception as e:
    e.KeyError: ModuleNotFoundError


def get_weather_info_by_city(city, units):
    if units == "c":
        weather = Weather(unit=Unit.CELSIUS)

    elif units == "f":
        weather = Weather(unit=Unit.FAHRENHEIT)

    else:
        print("none or wrong units selected")
        exit(1)

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

    return full_forecast_info


@click.command()
@click.option("--city", help="selected city")
@click.option("--units", type=click.Choice(['c', 'f']), help="select 'c' for Celsius or 'f' for Fahrenhiet.")
@click.option("--forecast", default=0, help="selected days , starting from today"
                                            "for example: --forecast TODAY for today's forecast, TODAY+3 for next 3 days")
def main(city, units, forecast):
    print(forecast)
    city_weather_info = get_weather_info_by_city(city, units)
    full_forecast_info = forecast_by_weather_info(city_weather_info)
    output = [full_forecast_info.get("condition"), full_forecast_info.get("high"), full_forecast_info.get("low")]
    for i in output:
        print(i[0])


if __name__ == "__main__":
    main()
