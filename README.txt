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

POST qilib jo'natamiz va ma'lumotlar bazaga jo'natiladi keyin tekon yaratiladi. Token har bir user uchun alohida shifrdan iborat bo'ladi.
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
Postman ilovasi orqali "Headers" bo'limi tanlang -> Key: Authorization, Value: Token 055a8fc71a0da76a2425aaa4223f31096b98bb6e  ma'lumotlar kiritilishi kerak. Token har userni uchun alohida aks etadi.
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

