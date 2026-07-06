import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env file
load_dotenv()

# Configure Gemini
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Load Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")


def ask_gemini(question, weather, prediction):

    prompt = f"""

You are an AI Disaster Management Expert.

Current Weather:

Temperature : {weather['temperature']} °C

Humidity : {weather['humidity']} %

Wind Speed : {weather['wind']} km/h

Pressure : {weather['pressure']} hPa

Rainfall : {weather['rain']} mm

Cloud Cover : {weather['cloud']} %

AI Prediction

Flood Risk : {prediction['Flood']} %

Cyclone Risk : {prediction['Cyclone']} %

Heatwave Risk : {prediction['Heatwave']} %

Landslide Risk : {prediction['Landslide']} %

User Question:

{question}

Give practical disaster management guidance.

Mention

• Immediate actions

• Safety precautions

• Emergency preparation

• Keep the answer simple.

"""

    response = model.generate_content(prompt)

    return response.text