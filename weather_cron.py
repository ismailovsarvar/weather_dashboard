"""
UZ: Terminal va *txt faylga ob-havo ma'lumotlarni yozish dasturini tuzamiz
EN: We will create a program to write weather data to a terminal and a *txt file
"""
import logging
import schedule
import time
import requests
import django
import os
from datetime import datetime
from django.core.cache import cache
from django.conf import settings

# UZ: Logging sozlamalari EN: Logging settings
logging.basicConfig(filename="weather_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

# Django muhitini yuklash # Loading the Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

"""
UZ: Olingan ma'lumotlarni terminalga chiqarish, so'ng txt faylga yozish
EN: Output the resulting data to the terminal, then write it to a *txt file
"""
def log_and_print(message, level="info"):
    print(message)
    if level == "info":
        logging.info(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)

def fetch_weather():
    
    # UZ: Foydalanuvchidan shahar nomlarini olish EN: Getting city names from the user
    cities_input = input("Enter city names separated by commas: ") # Shaharlarni nomlarini vergul bilan ajratib kiriting
    cities = cities_input.split(",") # UZ: Shaharlarni vergul bilan ajratib, listga aylantiramiz EN: We convert cities into a list, separating them with commas.

    log_and_print("Getting weather data...")

    # cities = ["Tashkent", "Sidney", "London"]
    api_key = getattr(settings, "WEATHER_API_KEY", None) 

    if not api_key:
        log_and_print("🛑 API token not configured!", "warning")
        return

    for city in cities:
        city = city.strip() # Shahar nomidan bo'sh joylarni olib tashlash
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            log_and_print(f"🛑 Error in query for {city}: {e}", "error")
            continue

        try:
            data = response.json()
            weather_info = {
                "name": data['location']['name'],
                "country": data['location']['country'],
                "lat": data['location']['lat'],
                "lon": data['location']['lon'],
                "temp_c": data['current']['temp_c'],
                "wind_kph": data['current']['wind_kph'],
                "cloud": data['current']['cloud'],
            }
            cache.set(f"weather_{city}", weather_info, timeout=3600)
            log_and_print(f"✅ Updated information for {city}: City name: {weather_info['name']}, Country name: {weather_info['country']}, lat: {weather_info['lat']}, lot: {weather_info['lon']}, Temp: {weather_info['temp_c']}°C, Wind: {weather_info['wind_kph']} km/h, Cloud: {weather_info['cloud']}%", "info")
        except KeyError as e:
            log_and_print(f"🛑 Error processing data for {city}: {e}", "warning")

# UZ: Har 1 daqiqada ishlashi uchun vazifani belgilaymiz 
# EN: We set the task to run every 1 minute
schedule.every(1).minutes.do(fetch_weather)

log_and_print("▶️  Skript ishga tushdi!", "info")

# UZ: Skript doimiy ishlashi uchun loop
# EN: Loop for continuous operation
while True:
    schedule.run_pending()
    log_and_print(f"⏳ [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Jarayonda...", "info")
    time.sleep(60)

