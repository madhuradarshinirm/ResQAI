import streamlit as st

from auth.login import login
from auth.session import (
    login_user,
    logout_user,
    is_logged_in
)

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="ResQAI",
    page_icon="🚨",
    layout="wide"
)

# -------------------------------------------------
# LOAD CSS
# -------------------------------------------------

def load_css():

    try:

        with open("assets/style.css") as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

    except FileNotFoundError:

        pass


load_css()

# -------------------------------------------------
# SESSION
# -------------------------------------------------

if "logged_in" not in st.session_state:

    st.session_state["logged_in"] = False

if "user" not in st.session_state:

    st.session_state["user"] = None

# =================================================
# LOGIN PAGE
# =================================================

if not is_logged_in():

    st.title("🚨 ResQAI")

    st.subheader("AI-Powered Disaster Management Platform")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("## 👤 Citizen Portal")

        st.write(
            """
Access:

- 🌦 Live Weather Updates
- 🗺 Disaster Map
- 🆘 SOS Emergency
- 🤖 AI Assistant
- 🏠 Shelter Finder
- 👥 Community Reports
"""
        )

    with col2:

        st.markdown("## 🏛 Disaster Control Center")

        st.write(
            """
Authorized disaster management officers can:

- 🚨 Monitor SOS Requests
- 👥 Verify Community Reports
- 📊 View Analytics Dashboard
- 🌍 Coordinate Emergency Response
"""
        )

    st.divider()

    st.subheader("🔐 Sign In")

    email = st.text_input(
        "Email Address"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    phone = st.text_input(
        "Phone Number"
    )

    address = st.text_area(
        "Address"
    )

    if st.button("🚀 Login"):

        user = login(
            email,
            password
        )

        if user:

            login_user(user)

            st.success(
                "Login Successful!"
            )

            st.rerun()

        else:

            st.error(
                "Invalid Email or Password."
            )

# =================================================
# HOME PAGE
# =================================================

else:

    user = st.session_state["user"]

    st.title("🚨 Welcome to ResQAI")

    st.success(
        f"Welcome, {user['name']}"
    )

    if user["email"].endswith("@gov.in"):

        st.info(
            "🏛 Logged in as Disaster Control Officer"
        )

    else:

        st.info(
            "👤 Logged in as Citizen"
        )

    st.divider()

    st.subheader("Available Modules")

    col1, col2 = st.columns(2)

    with col1:

        st.success("🌦 Live Weather")

        st.success("🗺 Disaster Map")

        st.success("🤖 AI Assistant")

        st.success("🆘 SOS Emergency")

    with col2:

        st.success("🏠 Shelter Finder")

        st.success("👥 Community Reports")

        st.success("📊 Dashboard")

    # ---------------------------------------------

    if user["email"].endswith("@gov.in"):

        st.divider()

        st.success(
            "👮 Disaster Control Center Access Granted"
        )

        st.page_link(
            "pages/Admin_Dashboard.py",
            label="🏛 Open Disaster Control Center",
            icon="🚨"
        )

    st.divider()

    if st.button("🚪 Logout"):

        logout_user()

        st.rerun()
