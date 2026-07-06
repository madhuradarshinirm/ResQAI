import requests

OVERPASS_URL = "https://overpass-api.de/api/interpreter"


def get_nearby_places(latitude, longitude):

    query = f"""
    [out:json];

    (

      node
        ["amenity"="hospital"]
        (around:5000,{latitude},{longitude});

      node
        ["amenity"="fire_station"]
        (around:5000,{latitude},{longitude});

      node
        ["amenity"="police"]
        (around:5000,{latitude},{longitude});

    );

    out;
    """

    response = requests.post(

        OVERPASS_URL,

        data=query,

        timeout=30

    )

    if response.status_code != 200:

        return []

    return response.json()["elements"]