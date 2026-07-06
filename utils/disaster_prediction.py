def predict_disaster(weather):

    temperature = weather["temperature"]
    humidity = weather["humidity"]
    wind = weather["wind"]
    rain = weather["rain"]
    pressure = weather["pressure"]
    cloud = weather["cloud"]

    result = {}

    # ==========================
    # Flood Risk
    # ==========================

    flood = 0

    if rain > 15:
        flood += 40

    if humidity > 85:
        flood += 20

    if cloud > 80:
        flood += 20

    if pressure < 1005:
        flood += 20

    result["Flood"] = min(flood,100)

    # ==========================
    # Cyclone Risk
    # ==========================

    cyclone = 0

    if wind > 35:
        cyclone += 45

    if pressure < 995:
        cyclone += 35

    if cloud > 80:
        cyclone += 20

    result["Cyclone"] = min(cyclone,100)

    # ==========================
    # Heatwave Risk
    # ==========================

    heat = 0

    if temperature > 38:
        heat += 60

    if humidity < 35:
        heat += 20

    if rain == 0:
        heat += 20

    result["Heatwave"] = min(heat,100)

    # ==========================
    # Landslide Risk
    # ==========================

    landslide = 0

    if rain > 20:
        landslide += 45

    if humidity > 85:
        landslide += 25

    if cloud > 80:
        landslide += 15

    if pressure < 1000:
        landslide += 15

    result["Landslide"] = min(landslide,100)

    return result