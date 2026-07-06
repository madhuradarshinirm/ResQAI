from datetime import datetime

from utils.firebase_config import get_firestore

db = get_firestore()


def create_sos(
    name,
    email,
    phone,
    city,
    latitude,
    longitude,
    disaster,
    risk
):

    data = {

        "name": name,

        "email": email,

        "phone": phone,

        "city": city,

        "latitude": latitude,

        "longitude": longitude,

        "disaster": disaster,

        "risk": risk,

        "status": "Pending",

        "created_at": datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

    }

    db.collection("sos_requests").add(data)

    return True