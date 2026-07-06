import streamlit as st

from utils.location import get_coordinates
from utils.weather import get_weather
from utils.disaster_prediction import predict_disaster
from utils.alerts import generate_alerts
from utils.session import initialize_session, save_data

st.set_page_config(
    page_title="Live Weather",
    layout="wide"
)

initialize_session()

st.title("🌦 Live Weather")

st.write(
    "Get real-time weather for any city in the world."
)

city = st.text_input(
    "Enter City Name",
    placeholder="Example: Mysuru"
)

if st.button("Get Live Weather"):

    if city.strip() == "":

        st.warning("Please enter a city.")

    else:

        location = get_coordinates(city)

        if location is None:

            st.error("City not found.")

        else:

            weather = get_weather(
                location["latitude"],
                location["longitude"]
            )

            if weather:

                st.success(location["display_name"])

                # -------------------------
                # Weather Metrics
                # -------------------------

                c1, c2, c3 = st.columns(3)

                with c1:

                    st.metric(
                        "🌡 Temperature",
                        f"{weather['temperature']} °C"
                    )

                    st.metric(
                        "💧 Humidity",
                        f"{weather['humidity']} %"
                    )

                with c2:

                    st.metric(
                        "💨 Wind",
                        f"{weather['wind']} km/h"
                    )

                    st.metric(
                        "🌍 Pressure",
                        f"{weather['pressure']} hPa"
                    )

                with c3:

                    st.metric(
                        "🌧 Rain",
                        f"{weather['rain']} mm"
                    )

                    st.metric(
                        "☁ Cloud Cover",
                        f"{weather['cloud']} %"
                    )

                st.divider()

                # -------------------------
                # AI Prediction
                # -------------------------

                st.subheader("🤖 AI Disaster Risk Analysis")

                prediction = predict_disaster(weather)

                alerts = generate_alerts(
                    weather,
                    prediction
                )

                save_data(
                    city,
                    location,
                    weather,
                    prediction,
                    alerts
                )

                left, right = st.columns(2)

                with left:

                    st.progress(prediction["Flood"] / 100)

                    st.write(
                        f"🌊 Flood Risk : {prediction['Flood']}%"
                    )

                    st.progress(prediction["Cyclone"] / 100)

                    st.write(
                        f"🌪 Cyclone Risk : {prediction['Cyclone']}%"
                    )

                with right:

                    st.progress(prediction["Heatwave"] / 100)

                    st.write(
                        f"🔥 Heatwave Risk : {prediction['Heatwave']}%"
                    )

                    st.progress(prediction["Landslide"] / 100)

                    st.write(
                        f"⛰ Landslide Risk : {prediction['Landslide']}%"
                    )

                st.divider()

                # -------------------------
                # Disaster Alerts
                # -------------------------

                st.subheader("🚨 Live Disaster Alerts")

                for alert in alerts:

                    if alert["level"] == "HIGH":

                        st.error(
                            f"""
### {alert['title']}

{alert['message']}
"""
                        )

                    elif alert["level"] == "MEDIUM":

                        st.warning(
                            f"""
### {alert['title']}

{alert['message']}
"""
                        )

                    else:

                        st.success(
                            f"""
### {alert['title']}

{alert['message']}
"""
                        )

            else:

                st.error("Weather service unavailable.")