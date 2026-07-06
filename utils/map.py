from utils.firebase_config import get_firestore

db = get_firestore()


def get_sos_locations():

    docs = db.collection("sos_requests").stream()

    data = []

    for doc in docs:

        item = doc.to_dict()

        data.append(item)

    return data


def get_report_locations():

    docs = db.collection("community_reports").stream()

    data = []

    for doc in docs:

        item = doc.to_dict()

        data.append(item)

    return data