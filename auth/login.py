from utils.firebase_config import get_firestore
import streamlit as st

db = get_firestore()

def login(email, password):

    doc = db.collection("users").document(email).get()

    if not doc.exists:
        st.error(f"Document not found: {email}")
        return None

    user = doc.to_dict()

    # SHOW THE DATA
    st.write("Firestore returned:")
    st.json(user)

    if "password" not in user:
        st.error("Password field missing!")
        return None

    if user["password"] != password:
        st.error("Wrong password")
        return None

    return user
