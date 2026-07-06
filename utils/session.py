import streamlit as st


def initialize_session():

    defaults = {

        "city": None,

        "location": None,

        "weather": None,

        "prediction": None,

        "alerts": None

    }

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value


def save_data(city, location, weather, prediction, alerts):

    st.session_state.city = city

    st.session_state.location = location

    st.session_state.weather = weather

    st.session_state.prediction = prediction

    st.session_state.alerts = alerts