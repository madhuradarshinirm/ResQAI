def generate_alerts(weather, prediction):

    alerts = []

    # Flood
    if prediction["Flood"] >= 70:
        alerts.append({
            "title": "🌊 Flood Alert",
            "level": "HIGH",
            "message": "Heavy rainfall detected. Move to higher ground and avoid rivers."
        })

    # Cyclone
    if prediction["Cyclone"] >= 60:
        alerts.append({
            "title": "🌪 Cyclone Alert",
            "level": "HIGH",
            "message": "Strong winds detected. Stay indoors and follow official advisories."
        })

    # Heatwave
    if prediction["Heatwave"] >= 60:
        alerts.append({
            "title": "🔥 Heatwave Alert",
            "level": "MEDIUM",
            "message": "Avoid going outside during afternoon hours. Stay hydrated."
        })

    # Landslide
    if prediction["Landslide"] >= 60:
        alerts.append({
            "title": "⛰ Landslide Alert",
            "level": "HIGH",
            "message": "Avoid hilly regions. Landslide possibility is high."
        })

    if len(alerts) == 0:
        alerts.append({
            "title": "✅ No Critical Alerts",
            "level": "SAFE",
            "message": "Current weather conditions do not indicate major disaster risks."
        })

    return alerts