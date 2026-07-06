import streamlit as st

st.set_page_config(
    page_title="Shelter Finder",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Emergency Shelter Finder")

st.write(
    "Find available emergency shelters and relief camps during disasters."
)

st.divider()

shelters = [

    {
        "name": "Government Higher Primary School Relief Camp",
        "city": "Mysuru",
        "capacity": 250,
        "occupied": 118,
        "food": "Available",
        "water": "Available",
        "electricity": "Available",
        "medical": "Available",
        "status": "Open"
    },

    {
        "name": "Community Hall Emergency Shelter",
        "city": "Mandya",
        "capacity": 180,
        "occupied": 172,
        "food": "Available",
        "water": "Available",
        "electricity": "Available",
        "medical": "Available",
        "status": "Nearly Full"
    },

    {
        "name": "District Sports Complex Shelter",
        "city": "Bengaluru",
        "capacity": 600,
        "occupied": 290,
        "food": "Available",
        "water": "Available",
        "electricity": "Available",
        "medical": "Available",
        "status": "Open"
    },

    {
        "name": "Relief Camp - Shivamogga",
        "city": "Shivamogga",
        "capacity": 350,
        "occupied": 330,
        "food": "Available",
        "water": "Available",
        "electricity": "Available",
        "medical": "Available",
        "status": "Nearly Full"
    }

]

for shelter in shelters:

    with st.container():

        st.subheader(shelter["name"])

        c1, c2 = st.columns(2)

        with c1:

            st.write(f"📍 **City:** {shelter['city']}")
            st.write(f"👥 **Capacity:** {shelter['capacity']}")
            st.write(f"🛏 **Occupied:** {shelter['occupied']}")

        with c2:

            st.write(f"🍛 **Food:** {shelter['food']}")
            st.write(f"🚰 **Water:** {shelter['water']}")
            st.write(f"⚡ **Electricity:** {shelter['electricity']}")
            st.write(f"🏥 **Medical Team:** {shelter['medical']}")

        if shelter["status"] == "Open":

            st.success("🟢 Status : Open")

        else:

            st.warning("🟡 Status : Nearly Full")

        st.button(
            f"📍 View Location - {shelter['city']}",
            key=shelter["name"]
        )

        st.divider()

st.info(
    """
Upcoming Improvements

✅ Real-time shelter availability

✅ Google Maps navigation

✅ Distance from your location

✅ Live occupancy

✅ Government disaster shelter integration
"""
)