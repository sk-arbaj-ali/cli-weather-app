import typer
import os
import requests
from dotenv import load_dotenv
from constants import URL,CURRENT_WEATHER
from typing_extensions import Annotated
from utilities import print_weather_data


app = typer.Typer(no_args_is_help=True)
load_dotenv()

@app.command()
def current_weather(
    city:Annotated[str, typer.Option(prompt="Provide the city name ",help="Provide city name")],
    aqi:Annotated[str, typer.Option(help="If you want air quality data provide 'yes'")] = "no"
    ):
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

if __name__ == "__main__":
    app()