# Week 11 Lab Exercise
# EU Capitals Weather Data Collection
# This program collects current and hourly weather data
# for all EU capital cities using the Open-Meteo API
# and saves the results into a structured JSON file.

import requests
import json
import time
from datetime import datetime

# LIST OF EU CAPITALS WITH COORDINATES

eu_cities = [
    {"city": "Vienna", "country": "Austria", "lat": 48.2082, "lon": 16.3738},
    {"city": "Brussels", "country": "Belgium", "lat": 50.8503, "lon": 4.3517},
    {"city": "Sofia", "country": "Bulgaria", "lat": 42.6977, "lon": 23.3219},
    {"city": "Zagreb", "country": "Croatia", "lat": 45.8150, "lon": 15.9819},
    {"city": "Nicosia", "country": "Cyprus", "lat": 35.1856, "lon": 33.3823},
    {"city": "Prague", "country": "Czechia", "lat": 50.0755, "lon": 14.4378},
    {"city": "Copenhagen", "country": "Denmark", "lat": 55.6761, "lon": 12.5683},
    {"city": "Tallinn", "country": "Estonia", "lat": 59.4370, "lon": 24.7536},
    {"city": "Helsinki", "country": "Finland", "lat": 60.1695, "lon": 24.9354},
    {"city": "Paris", "country": "France", "lat": 48.8566, "lon": 2.3522},
    {"city": "Berlin", "country": "Germany", "lat": 52.5200, "lon": 13.4050},
    {"city": "Athens", "country": "Greece", "lat": 37.9838, "lon": 23.7275},
    {"city": "Budapest", "country": "Hungary", "lat": 47.4979, "lon": 19.0402},
    {"city": "Dublin", "country": "Ireland", "lat": 53.3498, "lon": -6.2603},
    {"city": "Rome", "country": "Italy", "lat": 41.9028, "lon": 12.4964},
    {"city": "Riga", "country": "Latvia", "lat": 56.9496, "lon": 24.1052},
    {"city": "Vilnius", "country": "Lithuania", "lat": 54.6872, "lon": 25.2797},
    {"city": "Luxembourg", "country": "Luxembourg", "lat": 49.6116, "lon": 6.1319},
    {"city": "Valletta", "country": "Malta", "lat": 35.8989, "lon": 14.5146},
    {"city": "Amsterdam", "country": "Netherlands", "lat": 52.3676, "lon": 4.9041},
    {"city": "Warsaw", "country": "Poland", "lat": 52.2297, "lon": 21.0122},
    {"city": "Lisbon", "country": "Portugal", "lat": 38.7223, "lon": -9.1393},
    {"city": "Bucharest", "country": "Romania", "lat": 44.4268, "lon": 26.1025},
    {"city": "Bratislava", "country": "Slovakia", "lat": 48.1486, "lon": 17.1077},
    {"city": "Ljubljana", "country": "Slovenia", "lat": 46.0569, "lon": 14.5058},
    {"city": "Madrid", "country": "Spain", "lat": 40.4168, "lon": -3.7038},
    {"city": "Stockholm", "country": "Sweden", "lat": 59.3293, "lon": 18.0686}
]

# WEATHER CODE DESCRIPTIONS

weather_meanings = {
    0: "Clear sky",
    1: "Mostly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    61: "Light rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Light snow",
    95: "Thunderstorm"
}


# FUNCTION TO REQUEST WEATHER DATA FROM API

def get_weather(lat, lon):
    """Send request to Open-Meteo API and return JSON data."""

    base_url = "https://api.open-meteo.com/v1/forecast"
    today_date = datetime.now().strftime("%Y-%m-%d")

    parameters = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "hourly": "temperature_2m,precipitation_probability,weathercode",
        "timezone": "auto",
        "start_date": today_date,
        "end_date": today_date
    }

    try:
        response = requests.get(base_url, params=parameters, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as error:
        print("Request failed:", error)
        return None

# MAIN COLLECTION FUNCTION

def collect_weather():
    """Loop through all EU capitals and gather weather data."""

    final_data = {}

    print("Starting weather collection...\n")

    for city_data in eu_cities:
        city = city_data["city"]
        country = city_data["country"]

        print("Fetching data for:", city)

        raw_data = get_weather(city_data["lat"], city_data["lon"])

        if raw_data:
            try:
                current = raw_data.get("current_weather", {})
                hourly = raw_data.get("hourly", {})

                # Structure the data properly
                structured = {
                    "country": country,
                    "coordinates": {
                        "latitude": city_data["lat"],
                        "longitude": city_data["lon"]
                    },
                    "current_weather": {
                        "temperature": current.get("temperature"),
                        "windspeed": current.get("windspeed"),
                        "weathercode": current.get("weathercode"),
                        "condition": weather_meanings.get(current.get("weathercode")),
                        "time": current.get("time")
                    },
                    "hourly_forecast": []
                }

                # Add hourly forecast entries
                if "time" in hourly:
                    for i in range(len(hourly["time"])):
                        structured["hourly_forecast"].append({
                            "time": hourly["time"][i],
                            "temperature": hourly["temperature_2m"][i],
                            "precipitation_probability": hourly["precipitation_probability"][i],
                            "weathercode": hourly["weathercode"][i]
                        })

                final_data[city] = structured
                print("Success:", city)

            except Exception as processing_error:
                print("Error processing data for", city, ":", processing_error)

        else:
            print("Skipping city due to API failure.")

        # Delay to respect API rate limits
        time.sleep(0.7)

    return final_data

# SAVE RESULTS TO JSON FILE

def save_json(data, filename):
    """Save dictionary data into a formatted JSON file."""

    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        print("\nWeather data saved to", filename)

    except IOError as file_error:
        print("File writing failed:", file_error)

# PROGRAM ENTRY POINT

def main():
    print("======================================")
    print(" EU Capitals Weather Data Collector ")
    print("======================================\n")

    weather_results = collect_weather()

    save_json(weather_results, "eu_weather_data.json")

    print("\nProcess completed.")


if __name__ == "__main__":
    main()