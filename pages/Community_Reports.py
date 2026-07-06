import streamlit as st
from utils.reports import save_report

st.set_page_config(
    page_title="Community Reports",
    layout="wide"
)

st.title("👥 Community Reports")
st.write("Report disasters happening around you.")
st.divider()

with st.form("report_form"):

    name = st.text_input("Full Name")

    email = st.text_input("Email")

    phone = st.text_input("Phone Number")

    city = st.text_input("City")

    disaster = st.selectbox(
        "Disaster Type",
        [
            "Flood",
            "Fire",
            "Cyclone",
            "Earthquake",
            "Landslide",
            "Road Accident",
            "Building Collapse",
            "Medical Emergency",
            "Other"
        ]
    )

    description = st.text_area(
        "Describe the Incident"
    )

    image = st.file_uploader(
        "Upload Image",
        type=["jpg", "jpeg", "png"]
    )

    submitted = st.form_submit_button("📤 Submit Report")

if submitted:

    if (
        name.strip() == ""
        or email.strip() == ""
        or phone.strip() == ""
        or city.strip() == ""
        or description.strip() == ""
        or image is None
    ):

        st.warning("Please fill all details.")

    else:

        try:

            save_report(
                name,
                email,
                phone,
                city,
                disaster,
                description,
                image
            )

            st.success("✅ Report Submitted Successfully!")
            st.balloons()

        except Exception as e:

            st.error(f"Error: {e}")