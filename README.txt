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

url: http://127.0.0.1:8000/api/weather/<cit_name>/ # Example: http://127.0.0.1:8000/api/weather/tashkent/  shahar nomi ixtiyoriy tanlash mumkin.

Postman ilovasi orqali "Headers" bo'limi tanlang -> Key: Authorization Value: Token 055a8fc71a0da76a2425aaa4223f31096b98bb6e  ma'lumotlar kiritilishi kerak. Token har userni uchun alohida aks etadi.

Model turida "GET" tanlanib urlga so'rov jo'natiladi va kiritilgan shahar bo'yicha JSON ma'lumotlar qaytadi.

Example: 
{
    "name": "Tashkent",
    "country": "Uzbekistan",
    "lat": 41.3167,
    "lon": 69.25,
    "temp_c": 2.1,
    "temp_color": "#E6F7FF",
    "wind_kph": 7.9,
    "wind_color": "#E0F7FA",
    "cloud": 0,
    "cloud_color": "#FFF9C4"
}

Agar User ro'yxatdan o'tmagan bo'lsa, so'rov amalga oshmaydi va xatolik haqida ma'lumot beradi.

{
    "detail": "Authentication credentials were not provided."
}

