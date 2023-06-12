import folium
import pandas as pd


def main():
    df = pd.read_csv("transformed_data.csv")
    map = folium.Map(location=[0, 0], zoom_start=2)

    for index, row in df.iterrows():
        city = row["city"]
        latitude = row["latitude"]
        longitude = row["longitude"]
        temperature = row["temperature"]

        # Create a marker with a popup displaying city name and temperature
        marker = folium.Marker(
            location=[latitude, longitude], popup=f"{city}: {temperature} °C"
        )
        marker.add_to(map)

    map.save("map.html")

if __name__=='__main__':
        main()
