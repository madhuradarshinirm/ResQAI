import os
from datetime import datetime

from utils.firebase_config import get_firestore

db = get_firestore()


def save_report(
    name,
    email,
    phone,
    city,
    disaster,
    description,
    image
):

    os.makedirs("uploads", exist_ok=True)

    filename = (
        datetime.now().strftime("%Y%m%d%H%M%S")
        + "_"
        + image.name
    )

    filepath = os.path.join(
        "uploads",
        filename
    )

    with open(filepath, "wb") as f:
        f.write(image.getbuffer())

    report = {

        "name": name,

        "email": email,

        "phone": phone,

        "city": city,

        "disaster": disaster,

        "description": description,

        "image": filepath,

        "status": "Pending",

        "time": datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

    }

    db.collection(
        "community_reports"
    ).add(report)

    return True