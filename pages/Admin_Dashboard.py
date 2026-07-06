import streamlit as st
import plotly.express as px
import pandas as pd

from utils.admin import (
    get_all_sos,
    get_all_reports,
    update_sos_status,
    update_report_status
)

st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="🚨",
    layout="wide"
)

# -------------------------------------------------
# LOGIN CHECK
# -------------------------------------------------

if "user" not in st.session_state:

    st.error("🔒 Please login first.")

    st.stop()

user = st.session_state["user"]

# Allow only Admin users

if user.get("role", "").lower() != "admin":

    st.error("🚫 Access Denied")

    st.stop()

# -------------------------------------------------
# TITLE
# -------------------------------------------------

st.title("🚨 Disaster Control Center")

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------

sos_data = get_all_sos()

report_data = get_all_reports()

total_sos = len(sos_data)

total_reports = len(report_data)

pending = len(
    [
        x for x in sos_data
        if x.get("status") == "Pending"
    ]
)

progress = len(
    [
        x for x in sos_data
        if x.get("status") == "In Progress"
    ]
)

completed = len(
    [
        x for x in sos_data
        if x.get("status") == "Completed"
    ]
)

# -------------------------------------------------
# METRICS
# -------------------------------------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric("🚨 Total SOS", total_sos)

c2.metric("🟡 Pending", pending)

c3.metric("🟠 In Progress", progress)

c4.metric("🟢 Completed", completed)

st.divider()

# -------------------------------------------------
# CHARTS
# -------------------------------------------------

left, right = st.columns(2)

with left:

    st.subheader("📊 SOS Status")

    chart_df = pd.DataFrame({

        "Status": [

            "Pending",

            "In Progress",

            "Completed"

        ],

        "Count": [

            pending,

            progress,

            completed

        ]

    })

    fig = px.pie(

        chart_df,

        names="Status",

        values="Count",

        hole=0.5

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

with right:

    st.subheader("🌍 Disaster Types")

    if total_sos > 0:

        df = pd.DataFrame(sos_data)

        fig = px.bar(

            df,

            x="disaster",

            title="Disaster Distribution"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    else:

        st.info("No SOS data available.")

st.divider()

# -------------------------------------------------
# SOS REQUESTS
# -------------------------------------------------

st.header("🚨 SOS Requests")

if total_sos == 0:

    st.info("No SOS Requests.")

else:

    for sos in sos_data:

        with st.expander(

            f"{sos.get('name')} - {sos.get('city')}"

        ):

            st.write("📧 Email :", sos.get("email"))

            st.write("📞 Phone :", sos.get("phone"))

            st.write("🌊 Disaster :", sos.get("disaster"))

            st.write("⚠ Risk Score :", sos.get("risk"))

            st.write("📍 Latitude :", sos.get("latitude"))

            st.write("📍 Longitude :", sos.get("longitude"))

            st.write("🕒 Time :", sos.get("created_at"))

            status = st.selectbox(

                "Update Status",

                [

                    "Pending",

                    "In Progress",

                    "Completed"

                ],

                index=[

                    "Pending",

                    "In Progress",

                    "Completed"

                ].index(

                    sos.get("status")

                ),

                key=sos["id"]

            )

            if st.button(

                "Update SOS",

                key="SOS"+sos["id"]

            ):

                update_sos_status(

                    sos["id"],

                    status

                )

                st.success("✅ SOS Updated Successfully")

                st.rerun()

st.divider()

# -------------------------------------------------
# COMMUNITY REPORTS
# -------------------------------------------------

st.header("👥 Community Reports")

if total_reports == 0:

    st.info("No Community Reports.")

else:

    for report in report_data:

        with st.expander(

            f"{report.get('name')} - {report.get('city')}"

        ):

            st.write("📝 Description")

            st.write(report.get("description"))

            st.write("🖼 Image")

            st.write(report.get("image"))

            st.write("Current Status :", report.get("status"))

            status = st.selectbox(

                "Update Report Status",

                [

                    "Pending",

                    "Approved",

                    "Rejected"

                ],

                index=[

                    "Pending",

                    "Approved",

                    "Rejected"

                ].index(

                    report.get("status")

                ),

                key="REPORT"+report["id"]

            )

            if st.button(

                "Update Report",

                key="BTN"+report["id"]

            ):

                update_report_status(

                    report["id"],

                    status

                )

                st.success("✅ Report Updated Successfully")

                st.rerun()