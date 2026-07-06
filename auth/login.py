from utils.firebase_config import get_firestore

db = get_firestore()


def login(email, password):

    doc = db.collection("users").document(email).get()

    if not doc.exists:
        raise Exception(f"Document not found: {email}")

    user = doc.to_dict()

    if "password" not in user:
        raise Exception(user)

    if user["password"] != password:
        return None

    return user
