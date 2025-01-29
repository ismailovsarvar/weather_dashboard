from django.urls import path
from .views import RegisterView, LoginView, WeatherAPIView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('weather/<str:city_name>/', WeatherAPIView.as_view(), name='weather-api'),
]