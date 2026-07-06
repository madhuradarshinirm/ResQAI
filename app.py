import streamlit as st

from auth.login import login
from auth.session import (
    login_user,
    logout_user,
    is_logged_in
)

st.set_page_config(
    page_title="ResQAI",
    page_icon="🚨",
    layout="wide"
)

# -----------------------------
# Session
# -----------------------------

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "user" not in st.session_state:
    st.session_state["user"] = None


# -----------------------------
# LOGIN PAGE
# -----------------------------

if not is_logged_in():

    st.title("🚨 ResQAI Login")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    phone = st.text_input("Phone Number")

    address = st.text_area("Address")

    if st.button("Login"):

        user = login(
            email,
            password
        )

        if user is None:

            st.error("Invalid Email or Password.")

        else:

            login_user(user)

            st.rerun()


# -----------------------------
# HOME PAGE
# -----------------------------

else:

    user = st.session_state["user"]

    st.title("🚨 Welcome to ResQAI")

    st.success(
        f"Welcome {user['name']}"
    )

    st.write(
        "You are successfully logged in."
    )

    st.divider()

    st.subheader("Available Modules")

    st.info("Use the left sidebar to access the application modules.")

    st.write("✔ Dashboard")

    st.write("✔ Live Weather")

    st.write("✔ Disaster Map")

    st.write("✔ AI Assistant")

    st.write("✔ SOS")

    st.write("✔ Community Reports")

    st.write("✔ Shelter Finder")

    # -----------------------------
    # Admin Access
    # -----------------------------

    if user["email"].endswith("@gov.in"):

        st.divider()

        st.success("👮 Admin Access Enabled")

        st.page_link(
            "pages/Admin_Dashboard.py",
            label="Open Admin Dashboard",
            icon="🚨"
        )

    st.divider()

    if st.button("Logout"):

        logout_user()

        st.rerun()