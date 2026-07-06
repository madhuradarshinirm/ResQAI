from geopy.geocoders import Nominatim

def get_coordinates(city):

    try:

        geolocator = Nominatim(
            user_agent="ResQAI_Disaster_Management_App",
            timeout=10
        )

        location = geolocator.geocode(city)

        if location is None:
            return None

        return {
            "latitude": location.latitude,
            "longitude": location.longitude,
            "display_name": location.address
        }

    except:
        return None
