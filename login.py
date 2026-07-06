from utils.firebase_config import get_firestore

db = get_firestore()


def login(email, password):

    doc = db.collection("users").document(email).get()

    if not doc.exists:
        return None

    user = doc.to_dict()

    if user["password"] != password:
        return None

    return user