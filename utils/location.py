import requests
import streamlit as st

def get_coordinates(city):

    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": city,
        "format": "json",
        "limit": 1
    }

    headers = {
        "User-Agent": "ResQAI-Hackathon"
    }

    try:

        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=10
        )

        st.write("Status:", response.status_code)

        st.write(response.text)

        if response.status_code != 200:
            return None

        data = response.json()

        if len(data) == 0:
            return None

        return {
            "latitude": float(data[0]["lat"]),
            "longitude": float(data[0]["lon"]),
            "display_name": data[0]["display_name"]
        }

    except Exception as e:
        st.error(e)
        return None
