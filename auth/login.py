from utils.firebase_config import get_firestore

db = get_firestore()


def login(email, password):

    doc = db.collection("users").document(email).get()

    if not doc.exists:
        raise Exception(f"Document not found: {email}")

    user = doc.to_dict()

    raise Exception(f"Firestore returned: {user}")
