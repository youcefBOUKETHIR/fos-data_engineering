import json
import time
import csv

import requests


def get_list_of_cities():
    with open("cities.json") as f:
        data = json.load(f)

    return data


def get_lat_lon(city):
    url = (
        "https://nominatim.openstreetmap.org/search?country=Algeria&city="
        + city
        + "&format=json"
    )

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[0].get("lat"), response.json()[0].get("lon")

    return "err"


def get_current_weather(lat, lon):
    url = (
        "https://api.open-meteo.com/v1/forecast?latitude="
        + lat
        + "&longitude="
        + lon
        + "&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
    )
    print(url)

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()

    return "err"


def get_weather_all_cities(cities):
    data = dict()
    for city in cities:
        lat, lon = get_lat_lon(city)
        res = get_current_weather(lat, lon)
        data[city] = res
    return data


def save_output_data(data_):
    unix_timestamp = int(time.time())
    output_filename = "raw_data_" + str(unix_timestamp) + ".json"
    with open(output_filename, "w") as f:
        json.dump(data_, f)


def main():
    cities = get_list_of_cities()
    print(cities)

    weather_data = get_weather_all_cities(cities)
    save_output_data(weather_data)

if __name__=='__main__':
        main()