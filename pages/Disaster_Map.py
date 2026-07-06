import streamlit as st
from streamlit_folium import st_folium

from utils.location import get_coordinates
from utils.map_utils import create_map
from utils.places import get_nearby_places
from utils.session import initialize_session

st.set_page_config(
    page_title="Disaster Map",
    layout="wide"
)

initialize_session()

st.title("🗺 Live Disaster Map")

st.write("Search any city to monitor the disaster region.")

# Show previously selected city

if st.session_state.location:

    st.success(
        f"📍 Current City : {st.session_state.city}"
    )

# -------------------------
# Session State
# -------------------------

if "map_data" not in st.session_state:
    st.session_state.map_data = None

# -------------------------
# Search Form
# -------------------------

with st.form("city_form"):

    city = st.text_input(
        "Enter City Name",
        placeholder="Example: Mysuru"
    )

    submitted = st.form_submit_button("Show Map")

# -------------------------
# Get Location
# -------------------------

if submitted:

    if city.strip() == "":

        st.warning("Please enter a city.")

    else:

        location = get_coordinates(city)

        if location:

            st.session_state.map_data = {

                "city": city,

                "display": location["display_name"],

                "lat": location["latitude"],

                "lon": location["longitude"]

            }

        else:

            st.error("Location not found.")

# -------------------------
# Display Map
# -------------------------

if st.session_state.map_data:

    st.success(st.session_state.map_data["display"])

    places = get_nearby_places(

    st.session_state.map_data["lat"],

    st.session_state.map_data["lon"]

    )

    disaster_map = create_map(

        st.session_state.map_data["lat"],

        st.session_state.map_data["lon"],

        st.session_state.map_data["city"],

        places

    )

    st_folium(

        disaster_map,

        use_container_width=True,

        height=700,

        returned_objects=[]

    )

st.divider()

st.subheader("📊 Live Disaster Statistics")

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("🆘 SOS", "12")

c2.metric("🏥 Hospitals", "5")

c3.metric("🏠 Shelters", "6")

c4.metric("👥 Reports", "8")

c5.metric("🟢 Safe Zones", "3")