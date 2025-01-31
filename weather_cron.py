"""Terminal va txt faylga ob-havo ma'lumotlarni yozish"""
import logging
import schedule
import time
import requests
import django
import os
from datetime import datetime
from django.core.cache import cache
from django.conf import settings

# Logging sozlamalari
logging.basicConfig(filename="weather_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

# Django muhitini yuklash
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

"""Olingan ma'lumotlarni terminalga chiqarish, so'ng txt faylga yozish"""
def log_and_print(message, level="info"):
    print(message)
    if level == "info":
        logging.info(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)

def fetch_weather():
    
    # Foydalanuvchidan shahar nomlarini olish
    cities_input = input("Shaharlarni nomlarini vergul bilan ajratib kiriting: ")
    cities = cities_input.split(",") # Shaharlarni vergul bilan ajratib, listga aylantiramiz

    log_and_print("Ob-havo ma'lumotlari olinmoqda...")

    # cities = ["Tashkent", "Sidney", "London"] # Shahar nomlari o'zgartirish mumkin
    api_key = getattr(settings, "WEATHER_API_KEY", None) 

    if not api_key:
        log_and_print("🛑 API token sozlanmagan!", "warning")
        return

    for city in cities:
        city = city.strip() # Shahar nomidan bo'sh joylarni olib tashlash
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            log_and_print(f"🛑 {city} uchun so'rovda xatolik: {e}", "error")
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
            log_and_print(f"✅ {city} uchun ma'lumot yangilandi: City name: {weather_info['name']}, Country name: {weather_info['country']}, lat: {weather_info['lat']}, lot: {weather_info['lon']}, Temp: {weather_info['temp_c']}°C, Wind: {weather_info['wind_kph']} km/h, Cloud: {weather_info['cloud']}%", "info")
        except KeyError as e:
            log_and_print(f"🛑 {city} uchun ma'lumotni qayta ishlashda xatolik: {e}", "warning")

# Har 1 daqiqada ishlashi uchun vazifani belgilaymiz
schedule.every(1).minutes.do(fetch_weather)

log_and_print("▶️  Skript ishga tushdi!", "info") # Har 1 daqiqada ob-havo ma'lumotlari yangilanib turadi

# Skript doimiy ishlashi uchun loop
while True:
    schedule.run_pending()
    log_and_print(f"⏳ [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Jarayonda...", "info")
    time.sleep(60)

