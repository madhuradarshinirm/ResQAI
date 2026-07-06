from utils.firebase_config import get_firestore
import streamlit as st

db = get_firestore()

def login(email, password):

    doc = db.collection("users").document(email).get()

    if not doc.exists:
        st.error(f"Document not found: {email}")
        return None

    user = doc.to_dict()

    st.write("Document data:")
    st.json(user)

    st.write("Keys:")
    st.write(list(user.keys()))

    return None
