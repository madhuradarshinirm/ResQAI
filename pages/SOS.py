import streamlit as st

from utils.location import get_coordinates
from utils.sos import create_sos

st.set_page_config(
    page_title="SOS",
    layout="wide"
)

st.title("🚨 Emergency SOS")

st.write(
    "Send an emergency request to the disaster management team."
)

name = st.text_input("Full Name")

email = st.text_input("Email")

phone = st.text_input("Phone Number")

city = st.text_input("Current City")

disaster = st.selectbox(

    "Emergency Type",

    [

        "Flood",

        "Cyclone",

        "Earthquake",

        "Landslide",

        "Fire",

        "Medical Emergency",

        "Other"

    ]

)

risk = st.slider(

    "Risk Level",

    0,

    100,

    50

)

if st.button("🚨 Send SOS"):

    location = get_coordinates(city)

    if location is None:

        st.error("City not found.")

    else:

        create_sos(

            name,

            email,

            phone,

            city,

            location["latitude"],

            location["longitude"],

            disaster,

            risk

        )

        st.success("🚨 SOS Sent Successfully!")

        st.balloons()