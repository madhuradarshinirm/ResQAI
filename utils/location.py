import requests
import streamlit as st

API_KEY = st.secrets["OPENWEATHER_API_KEY"]

def get_coordinates(city):

    url = "https://api.openweathermap.org/geo/1.0/direct"

    params = {
        "q": city,
        "limit": 1,
        "appid": API_KEY
    }

    response = requests.get(url, params=params, timeout=10)

    if response.status_code != 200:
        return None

    data = response.json()

    if not data:
        return None

    return {
        "latitude": data[0]["lat"],
        "longitude": data[0]["lon"],
        "display_name": f"{data[0]['name']}, {data[0]['country']}"
    }
