Postman ilovasi orqali:

=================================================
Bu muhim! -->> Terminal orqali Serverni ("py manage.py runserver") ishga tushirilishi kerak.

Userni register qilish linki: http://127.0.0.1:8000/api/register/

Metod turiga "POST" tanlanadi.
JSON ma'lumotlarni kiritish uchun "Body" bo'limi -> "raw" -> JSON turi tanlash lozim.
Body qismga json shaklda user ma'lumotlar kiritiladi:
{
    "username": "jhonuser",
    "password": "jhon123",
    "first_name": "John",
    "last_name": "Doe"
}

POST qilib jo'natamiz va ma'lumotlar bazaga jo'natiladi keyin tekon yaratiladi. 
Token har bir user uchun alohida shifrdan iborat bo'ladi.
Quyidagicha:

{
    "token": "f1473bcfcd2139a4947c29445cf1f102ee1c8a44"
}

=================================================
Userni login qilish
Metod turiga "POST" tanlanadi.
JSON ma'lumotlarni kiritish uchun "Body" -> "raw" -> JSON turi tanlash lozim.

url: http://127.0.0.1:8000/api/login/

Body qismga json shaklda user ma'lumotlar kiritiladi:

{
    "username": "jhonuser",
    "password": "jhon123"
}

POST qilib jo'natiladi va ma'lumotlar bazasidan mavjud userni chaqiradi va token shaklda ma'lumot qaytdadi.

=================================================
Authentication orqali ob-havo ma'lumotlarni olish.

GET orqali bitta shahar ob-havosi olinadi.
POST orqali bir nechta shaharlarni ma'lumoti olinadi.

url: http://127.0.0.1:8000/api/weather/
Metod: POST
Postman ilovasi orqali "Headers" bo'limi tanlang -> Key: Authorization, Value: Token 055a8fc71a0da76a2425aaa4223f31096b98bb6e  ma'lumotlar kiritilishi kerak. 
Token har userni uchun alohida aks etadi.
Body'ga (JSON formatda):
{
  "cities": ["Tashkent", "London"]
}

Javob (Response) shunday bo‘ladi: 
[
   {
      "name": "Tashkent",
      "country": "Uzbekistan",
      "lat": 41.2995,
      "lon": 69.2401,
      "temp_c": 10.5,
      "temp_color": "#FF5733",
      "wind_kph": 5.2,
      "wind_color": "#00A2E8",
      "cloud": 20,
      "cloud_color": "#CCCCCC"
   },
   {
      "name": "London",
      "country": "United Kingdom",
      "lat": 51.5074,
      "lon": -0.1278,
      "temp_c": 8.3,
      "temp_color": "#FFD700",
      "wind_kph": 10.4,
      "wind_color": "#008000",
      "cloud": 50,
      "cloud_color": "#999999"
   }
]

Agar User ro'yxatdan o'tmagan bo'lsa, so'rov amalga oshmaydi va xatolik haqida ma'lumot beradi.

{
    "detail": "Authentication credentials were not provided."
}

CRON JOB ishlatish
weather_cron.py fayl yaratildi.
CRONTAB script yaratilib, olingan ma'lumotlarni ham terminalda ko'rsatadi ham *txt faylga yozib boradi.
Har 1 minutda ob-havo ma'lumotlarni yangilab turish uchun dastur tuzamiz. 
Vaqtni siz ixtiyoriy belgilashingiz mumkin. Test uchun 1 daqiqa tanlandi.

schedule.every(<time>).minutes.do(fetch_weather) -> <time> ga siz qo'ymoqchi bo'lgan vaqt qiymati.

Eslatma! Kiritilgan qiymat minutlarda o'lchanadi, 1 soatga belgilamoqchi bo'lsangiz 60 daqiqa qilib qiymat kiritasiz.

Dasturni ishga tushirish uchun Terminalni ochib "python weather_cron.py" scriptni kiritasiz.
While Loop orqali siz kiritgan vaqt va shaharlar nomi asosida ob-havo ma'lumotlarni yangilab turadi.

EXAMPLE:

input: Tashkent, Sidney, London
Result: 
▶️  Skript ishga tushdi!
⏳ [2025-01-31 13:25:11] Jarayonda... 
# Bu muhim! Jarayon vaqtda biroz kutiladi.

Shaharlarni nomlarini vergul bilan ajratib kiriting: Tashkent, Sidney, London
Ob-havo ma'lumotlari olinmoqda...
✅ Tashkent uchun ma'lumot yangilandi: City name: Tashkent, Country name: Uzbekistan, lat: 41.3167, lot: 69.25, Temp: 2.4°C, Wind: 5.8 km/h, Cloud: 100%
✅ Sidney uchun ma'lumot yangilandi: City name: Sidney, Country name: United States of America, lat: 40.2842, lot: -84.1556, Temp: 5.3°C, Wind: 14.8 km/h, Cloud: 100%
✅ London uchun ma'lumot yangilandi: City name: London, Country name: United Kingdom, lat: 51.5171, lot: -0.1062, Temp: 5.4°C, Wind: 13.7 km/h, Cloud: 75%
