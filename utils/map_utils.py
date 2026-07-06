import folium


def create_map(latitude, longitude, city, places):

    disaster_map = folium.Map(
        location=[latitude, longitude],
        zoom_start=13
    )

    # -----------------------------
    # Selected City
    # -----------------------------

    folium.Marker(
        [latitude, longitude],
        popup=f"📍 {city}",
        tooltip="Selected City",
        icon=folium.Icon(
            color="blue",
            icon="info-sign"
        )
    ).add_to(disaster_map)

    # -----------------------------
    # Disaster Zone
    # -----------------------------

    folium.Circle(
        location=[latitude, longitude],
        radius=5000,
        color="red",
        fill=True,
        fill_color="red",
        fill_opacity=0.25,
        popup="🚨 Disaster Zone"
    ).add_to(disaster_map)

    # -----------------------------
    # Safe Zone
    # -----------------------------

    folium.Circle(
        location=[
            latitude + 0.04,
            longitude + 0.04
        ],
        radius=1200,
        color="green",
        fill=True,
        fill_color="green",
        fill_opacity=0.35,
        popup="🟢 Safe Zone"
    ).add_to(disaster_map)

    # -----------------------------
    # Hospital
    # -----------------------------

    folium.Marker(
        [latitude + 0.02, longitude - 0.02],
        popup="🏥 Government Hospital",
        tooltip="Hospital",
        icon=folium.Icon(
            color="red",
            icon="plus",
            prefix="fa"
        )
    ).add_to(disaster_map)

    # -----------------------------
    # Police Station
    # -----------------------------

    folium.Marker(
        [latitude - 0.02, longitude + 0.02],
        popup="🚓 Police Station",
        tooltip="Police",
        icon=folium.Icon(
            color="blue",
            icon="shield",
            prefix="fa"
        )
    ).add_to(disaster_map)

    # -----------------------------
    # Fire Station
    # -----------------------------

    folium.Marker(
        [latitude + 0.01, longitude + 0.04],
        popup="🚒 Fire Station",
        tooltip="Fire Station",
        icon=folium.Icon(
            color="orange",
            icon="fire",
            prefix="fa"
        )
    ).add_to(disaster_map)

    # -----------------------------
    # Shelter
    # -----------------------------

    folium.Marker(
        [latitude - 0.03, longitude - 0.03],
        popup="🏠 Emergency Shelter",
        tooltip="Shelter",
        icon=folium.Icon(
            color="green",
            icon="home",
            prefix="fa"
        )
    ).add_to(disaster_map)

    # -----------------------------
    # SOS Request
    # -----------------------------

    folium.Marker(
        [latitude + 0.015, longitude - 0.015],
        popup="🆘 SOS Request",
        tooltip="Citizen Needs Help",
        icon=folium.Icon(
            color="darkred",
            icon="warning-sign"
        )
    ).add_to(disaster_map)

    # -----------------------------
    # Community Report
    # -----------------------------

    folium.Marker(
        [latitude - 0.015, longitude + 0.015],
        popup="👥 Community Report",
        tooltip="Flood Report",
        icon=folium.Icon(
            color="purple",
            icon="info-sign"
        )
    ).add_to(disaster_map)

    # -----------------------------
    # Nearby Places from Overpass
    # -----------------------------

    for place in places:

        lat = place["lat"]
        lon = place["lon"]

        tags = place.get("tags", {})

        name = tags.get("name", "Unknown")

        amenity = tags.get("amenity", "")

        color = "gray"
        icon = "info-sign"

        if amenity == "hospital":
            color = "red"
            icon = "plus"

        elif amenity == "police":
            color = "blue"
            icon = "shield"

        elif amenity == "fire_station":
            color = "orange"
            icon = "fire"

        elif amenity in [
            "school",
            "community_centre",
            "townhall"
        ]:
            color = "green"
            icon = "home"

        folium.Marker(
            [lat, lon],
            popup=name,
            tooltip=amenity.title() if amenity else "Place",
            icon=folium.Icon(
                color=color,
                icon=icon,
                prefix="fa"
            )
        ).add_to(disaster_map)

    # -----------------------------
    # Legend
    # -----------------------------

    legend = """
    <div style="
    position: fixed;
    bottom: 30px;
    left: 30px;
    width: 240px;
    background: white;
    border:2px solid grey;
    z-index:9999;
    padding:10px;
    font-size:14px;
    border-radius:8px;
    ">

    <b>🗺 Map Legend</b><br><br>

    🔵 Selected City<br>
    🔴 Disaster Zone<br>
    🟢 Safe Zone<br>
    🏥 Hospital<br>
    🚓 Police Station<br>
    🚒 Fire Station<br>
    🏠 Shelter<br>
    🆘 SOS Request<br>
    👥 Community Report

    </div>
    """

    disaster_map.get_root().html.add_child(
        folium.Element(legend)
    )

    return disaster_map