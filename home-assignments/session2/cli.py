try:
    import click
    from weather import Weather, Unit
except Exception as e:
    e.KeyError: ModuleNotFoundError


# TODO change date format
# TODO fix --units (need to be -c or -f)


def get_weather_info_by_city(city, units):
    weather = Weather()
    selected_units = ""
    if units == "c":
        weather = Weather(unit=Unit.CELSIUS)
        selected_units = "Celsius"

    elif units == "f":
        weather = Weather(unit=Unit.FAHRENHEIT)
        selected_units = "Fahrenheit"

    else:
        print("none or wrong units selected")
        exit(1)

    city_weather_info = weather.lookup_by_location(city)

    return city_weather_info, selected_units


def forecast_by_weather_info(city_weather_info):
    forecasts = city_weather_info.forecast
    dates = []
    condition = []
    high = []
    low = []
    for forecast in forecasts:
        dates.append(forecast.date)
        condition.append(forecast.text)
        high.append(forecast.high)
        low.append(forecast.low)

    full_forecast_info = {"date": dates, "condition": condition, "high": high, "low": low}

    return full_forecast_info


def parse_output_from_weather_info(full_forecast_info, forecast):
    output = [full_forecast_info.get("date"), full_forecast_info.get("condition"), full_forecast_info.get("high"),
              full_forecast_info.get("low")]
    ranged_forecast = []
    for i in range(0, forecast + 1):
        daily_forecast = []
        for day in output:
            daily_forecast.append(day[i])
        ranged_forecast.append(daily_forecast)

    return ranged_forecast


def get_forecast_length(forecast):
    split_forecast = forecast.split("+")
    if len(split_forecast) == 1:
        forecast_length = 0
    else:
        forecast_length = int(split_forecast[1])

    if forecast_length > 9:
        print("Required forecast in unknown, forecast of up to 10 days may be displayed")
        exit(1)

    return forecast_length


@click.command()
@click.option("--city", help="selected city")
@click.option("--units", type=click.Choice(['c', 'f']), help="select 'c' for Celsius or 'f' for Fahrenhiet.")
@click.option("--forecast", required=False, default="TODAY", show_default=True,
              help="selected days , starting from today"
                   "for example: --forecast TODAY for today's forecast, TODAY+3 for next 3 days")
def main(city, units, forecast):
    forecast = get_forecast_length(forecast)
    city_weather_info, units = get_weather_info_by_city(city, units)
    full_forecast_info = forecast_by_weather_info(city_weather_info)
    ranged_forecast = parse_output_from_weather_info(full_forecast_info, forecast)

    if forecast == 0:
        condition = ranged_forecast[0][1]
        high = ranged_forecast[0][2]
        low = ranged_forecast[0][3]
        output_string = "The weather in {city} today is {condition} with temperatures trailing from ({low})-({high}) " \
                        "{units}".format(city=city, condition=condition, high=high, low=low, units=units)
        print(output_string)

    else:
        for i in range(0, forecast + 1):
            date = ranged_forecast[i][0]
            condition = ranged_forecast[i][1]
            high = ranged_forecast[i][2]
            low = ranged_forecast[i][3]
            output_string = "{date} {condition} with temperatures trailing from ({low})-({high}) {units}".format(
                date=date,
                city=city, condition=condition, high=high, low=low, units=units)
            print(output_string)
    return 0


if __name__ == "__main__":
    main()
