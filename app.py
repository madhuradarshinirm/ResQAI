import streamlit as st

from auth.login import login
from auth.session import (
    login_user,
    logout_user,
    is_logged_in
)

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="ResQAI",
    page_icon="🚨",
    layout="wide"
)

# ---------------------------------------------------
# LOAD CSS
# ---------------------------------------------------

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

# ---------------------------------------------------
# SESSION
# ---------------------------------------------------

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False

if "user" not in st.session_state:

    st.session_state.user = None


# ===================================================
# LOGIN PAGE
# ===================================================

if not is_logged_in():

    st.markdown(
        """
# 🚨 ResQAI

### AI-Powered Disaster Management Platform
"""
    )

    st.divider()

    left, right = st.columns(2)

    # ------------------------------------------------

    with left:

        st.markdown("## 👤 Citizen Portal")

        st.success(
            """
### Demo Account

📧 **Email**

`citizen@gmail.com`

🔑 **Password**

`citizen123`
"""
        )

    # ------------------------------------------------

    with right:

        st.markdown("## 🏛 Disaster Control Center")

        st.success(
            """
### Demo Account

📧 **Email**

`admin@gov.in`

🔑 **Password**

`admin123`
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
        "Phone Number (Optional)"
    )

    address = st.text_area(
        "Address (Optional)"
    )

    if st.button("🚀 Login"):

        user = login(
            email,
            password
        )

        if user:

            login_user(user)

            st.success(
                f"Welcome {user['name']}"
            )

            st.rerun()

        else:

            st.error(
                "Invalid Email or Password."
            )

# ===================================================
# HOME PAGE
# ===================================================

else:

    user = st.session_state.user

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

    st.subheader("📦 Available Modules")

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

    # ------------------------------------------------

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

    st.markdown("### 🚀 Quick Navigation")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.page_link(
            "pages/Dashboard.py",
            label="📊 Dashboard"
        )

        st.page_link(
            "pages/Live_Weather.py",
            label="🌦 Live Weather"
        )

        st.page_link(
            "pages/Disaster_Map.py",
            label="🗺 Disaster Map"
        )

    with c2:

        st.page_link(
            "pages/AI_Assistant.py",
            label="🤖 AI Assistant"
        )

        st.page_link(
            "pages/SOS.py",
            label="🆘 SOS"
        )

        st.page_link(
            "pages/Community_Reports.py",
            label="👥 Community Reports"
        )

    with c3:

        st.page_link(
            "pages/Shelter_Finder.py",
            label="🏠 Shelter Finder"
        )

    st.divider()

    if st.button("🚪 Logout"):

        logout_user()

        st.rerun()
