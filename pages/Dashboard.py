import streamlit as st

from utils.admin import (
    get_dashboard_stats
)

st.set_page_config(
    page_title="Dashboard",
    page_icon="🚨",
    layout="wide"
)

# -----------------------------------
# LOGIN CHECK
# -----------------------------------

if "user" not in st.session_state:

    st.error("Please login first.")

    st.stop()

user = st.session_state["user"]

# -----------------------------------
# LOAD STATS
# -----------------------------------

stats = get_dashboard_stats()

# -----------------------------------
# HEADER
# -----------------------------------

st.title("🚨 ResQAI")

st.caption(
    "AI Powered Disaster Management Platform"
)

st.success(
    f"Welcome, {user['name']}"
)

st.write(
    f"Role : **{user['role']}**"
)

st.divider()

# -----------------------------------
# LIVE STATISTICS
# -----------------------------------

st.subheader("📊 Live Statistics")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "🆘 SOS Requests",
    stats["total_sos"]
)

c2.metric(
    "👥 Community Reports",
    stats["reports"]
)

c3.metric(
    "🟡 Pending",
    stats["pending"]
)

c4.metric(
    "🟢 Completed",
    stats["completed"]
)

st.divider()

# -----------------------------------
# QUICK ACTIONS
# -----------------------------------

st.subheader("🚀 Quick Actions")

col1, col2, col3 = st.columns(3)

with col1:

    st.page_link(
        "pages/Live_Weather.py",
        label="🌦 Live Weather"
    )

    st.page_link(
        "pages/Disaster_Map.py",
        label="🗺 Disaster Map"
    )

with col2:

    st.page_link(
        "pages/SOS.py",
        label="🆘 Send SOS"
    )

    st.page_link(
        "pages/Community_Reports.py",
        label="👥 Report Disaster"
    )

with col3:

    st.page_link(
        "pages/Shelter_Finder.py",
        label="🏠 Shelter Finder"
    )

    st.page_link(
        "pages/AI_Assistant.py",
        label="🤖 AI Assistant"
    )

# Show Admin Dashboard only for admins
if user.get("role", "").lower() == "admin":

    st.page_link(
        "pages/Admin_Dashboard.py",
        label="👮 Admin Dashboard"
    )

st.divider()

# -----------------------------------
# DISASTER SAFETY ALERT
# -----------------------------------

st.subheader("⚠ Disaster Safety Reminder")

st.warning(
    """
• Follow official government advisories.

• Avoid flooded roads and damaged buildings.

• Keep emergency supplies ready.

• Use SOS only during genuine emergencies.

• Stay calm and help others if it is safe.
"""
)

st.divider()

# -----------------------------------
# EMERGENCY CONTACTS
# -----------------------------------

st.subheader("📞 National Emergency Contacts")

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.info(
        """
🚑 Ambulance

108
"""
    )

with c2:

    st.info(
        """
👮 Police

100
"""
    )

with c3:

    st.info(
        """
🚒 Fire

101
"""
    )

with c4:

    st.info(
        """
🆘 National Emergency

112
"""
    )

st.divider()

# -----------------------------------
# ABOUT
# -----------------------------------

st.subheader("ℹ About ResQAI")

st.write(
    """
ResQAI is an AI-powered disaster management platform that helps citizens
and emergency authorities respond quickly during disasters using
real-time weather monitoring, AI-based disaster prediction,
community reporting, shelter information, SOS requests,
and an intelligent emergency assistant.
"""
)

st.success("✅ System Status : ONLINE")