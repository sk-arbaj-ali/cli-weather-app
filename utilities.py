
def print_weather_data(location,current):
    print(f"Location name : {location['name']}")
    print(f"Region name : {location['region']}")
    print(f"Country name : {location['country']}")
    print(f"TimeZone : {location['tz_id']}")
    print(f"Weather last-updated : {current['last_updated']}")
    print(f"Temperature in celcius : {current['temp_c']}")
    print(f"Temperature in farenheight : {current['temp_f']}")
    print(f"Weather condition : {current['condition']['text']}")
    print(f"Wind direction and speed(kph) : {current['wind_dir']} {current['wind_kph']}")
    print(f"Humidity : {current['humidity']}")
    
    if current.get("air_quality", None) :
        print(f"Carbon Monoxide (μg/m3) : {current.get('air_quality')['co']}")
        print(f"Ozone (μg/m3) : {current.get('air_quality')['o3']}")
        print(f"Nitrogen dioxide (μg/m3) : {current.get('air_quality')['no2']}")

