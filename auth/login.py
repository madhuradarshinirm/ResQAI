from utils.firebase_config import get_firestore

db = get_firestore()


def login(email, password):

    doc = db.collection("users").document(email).get()

    if not doc.exists:
        print("Document not found:", email)
        return None

    user = doc.to_dict()

    print("User data:", user)

    if "password" not in user:
        print("Password field missing!")
        return None

    if user["password"] != password:
        print("Wrong password")
        return None

    return user
