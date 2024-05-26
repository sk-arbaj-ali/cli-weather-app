import typer
import os
import requests
from dotenv import load_dotenv
from constants import URL,CURRENT_WEATHER,FORECAST
from typing_extensions import Annotated
from utilities import print_weather_data
from requests.exceptions import RequestException, ConnectionError


app = typer.Typer(no_args_is_help=True)
load_dotenv()

@app.command()
def forecast_weather(
    city:Annotated[str, typer.Option(prompt="Provide the city name ",help="Provide city name")],
    days:Annotated[int, typer.Option(prompt="Number of days of weather forecast. Value ranges from 1 to 10")]=1,
    aqi:Annotated[str, typer.Option(help="If you want air quality data provide 'yes'")] = "no"
    ):
    '''
    Use this command to check weather forecast data.
    provide city, days and aqi information.
    '''
    try:
        response = requests.get(
        f"{URL}{FORECAST}",
        params={"key":os.getenv("API_KEY"),"q":city,"days":days,"aqi":aqi}
        )
        response.raise_for_status()
        json_response = response.json()
        location_data = json_response["location"]
        current_data = json_response["current"]
        forecastday = json_response["forecast"]["forecastday"]
        print_weather_data(location_data,current_data,forecastday)
    except requests.HTTPError:
        json_response = response.json()
        print(f"Response status code : {response.status_code}")
        print(f"error : {json_response['error']['message']}")
    except ConnectionError:
        print(f"error : a connection error has occurred.")
        print(f"remarks : please check your internet connection.")
    except RequestException as err:
        print(f"error : Some error has occurred.")
        print(f"remarks : please contact to developers.")


@app.command()
def current_weather(
    city:Annotated[str, typer.Option(prompt="Provide the city name ",help="Provide city name")],
    aqi:Annotated[str, typer.Option(help="If you want air quality data provide 'yes'")] = "no"
    ):
    '''
    Use this command to check the current weather.
    Provide the city name and aqi information.
    '''
    try:
        response = requests.get(
        f"{URL}{CURRENT_WEATHER}",
        params={"key":os.getenv("API_KEY"),"q":city,"aqi":aqi}
        )
        response.raise_for_status()
        json_response = response.json()
        location_data = json_response["location"]
        current_data = json_response["current"]
        print_weather_data(location_data,current_data)
    except requests.HTTPError:
        json_response = response.json()
        print(f"Response status code : {response.status_code}")
        print(f"error : {json_response['error']['message']}")
    except ConnectionError:
        print(f"error : a connection error has occurred.")
        print(f"remarks : please check your internet connection.")
    except RequestException as err:
        print(f"error : Some error has occurred.")
        print(f"remarks : please contact to developers.")

@app.callback()
def main():
    '''
        This is a cli weather app for realtime weather data.
    '''

if __name__ == "__main__":
    app()