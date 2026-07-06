import firebase_admin

from firebase_admin import credentials

from firebase_admin import firestore


def get_firestore():

    if not firebase_admin._apps:

        cred = credentials.Certificate(
            "firebase/serviceAccountKey.json"
        )

        firebase_admin.initialize_app(cred)

    db = firestore.client()

    return db