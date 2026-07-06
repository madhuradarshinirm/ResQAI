from utils.firebase_config import get_firestore

db = get_firestore()


# =====================================================
# SOS REQUESTS
# =====================================================

def get_all_sos():

    docs = db.collection("sos_requests").stream()

    data = []

    for doc in docs:

        item = doc.to_dict()

        item["id"] = doc.id

        data.append(item)

    return data


def update_sos_status(document_id, status):

    db.collection(
        "sos_requests"
    ).document(document_id).update(

        {
            "status": status
        }

    )


def get_sos_count():

    return len(get_all_sos())


# =====================================================
# COMMUNITY REPORTS
# =====================================================

def get_all_reports():

    docs = db.collection(
        "community_reports"
    ).stream()

    data = []

    for doc in docs:

        item = doc.to_dict()

        item["id"] = doc.id

        data.append(item)

    return data


def update_report_status(document_id, status):

    db.collection(
        "community_reports"
    ).document(document_id).update(

        {
            "status": status
        }

    )


def get_report_count():

    return len(get_all_reports())


# =====================================================
# DASHBOARD ANALYTICS
# =====================================================

def get_dashboard_stats():

    sos = get_all_sos()

    reports = get_all_reports()

    pending = len(

        [

            x

            for x in sos

            if x.get("status") == "Pending"

        ]

    )

    in_progress = len(

        [

            x

            for x in sos

            if x.get("status") == "In Progress"

        ]

    )

    completed = len(

        [

            x

            for x in sos

            if x.get("status") == "Completed"

        ]

    )

    return {

        "total_sos": len(sos),

        "pending": pending,

        "in_progress": in_progress,

        "completed": completed,

        "reports": len(reports)

    }