import requests


def get_weather(latitude, longitude):

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current="
        "temperature_2m,"
        "relative_humidity_2m,"
        "surface_pressure,"
        "wind_speed_10m,"
        "precipitation,"
        "cloud_cover"
    )

    response = requests.get(
        url,
        timeout=10
    )

    if response.status_code != 200:
        return None

    data = response.json()

    current = data["current"]

    return {

        "temperature": current["temperature_2m"],

        "humidity": current["relative_humidity_2m"],

        "pressure": current["surface_pressure"],

        "wind": current["wind_speed_10m"],

        "rain": current["precipitation"],

        "cloud": current["cloud_cover"]

    }