import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer
from .models import TemperatureColor, WindColor, CloudColor
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated

"""
UZ: Register va Login uchun APIView yaratish: 
EN: Create APIView for Register and Login:
"""

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({"token": token.key}, status=status.HTTP_200_OK)
            return Response({"Error": "Incorrect account information"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def post(self, request):
    serializer = RegisterSerializer(data=request.data)
    # Agar serializerdan noto'g'ri model bo'lsa, bu xato keltiradi 
    # If an incorrect model is used in the serializer, it will result in an error
    if serializer.is_valid():
        user = serializer.save()  
        return Response({"message": "User created successfully"})
    return Response(serializer.errors, status=400)


"""
UZ: Ob-havo ma'lumotlarini olish uchun APIView yaratish:
EN: Create a APIView to collect weather data:
"""
class WeatherAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_weather_color(self, model, value, min_field, max_field, default_color="#FFFFFF"):
        # Ko'rsatilgan qiymatga mos rangni qaytaradi.
        # Returns the color corresponding to the specified value.
        filter_kwargs = {f"{min_field}__lte": value, f"{max_field}__gte": value}
        color = model.objects.filter(**filter_kwargs).first()
        return color.hex_code if color else default_color

    def get(self, request, city_name):
        # API tokenni settings orqali olish
        # Get an API token in settings
        api_key = getattr(settings, "WEATHER_API_KEY", None)
        if not api_key:
            return Response({"error": "API token sozlanmagan"}, status=500)

        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}"
        response = requests.get(url)

        """
        UZ: Xatolik chiqib qolsa, xatolikni tashlash uchun
        EN: To discard the error if one occurs
        """
        if response.status_code != 200:
            error_message = response.json().get("error", {}).get("message", "Information not found!")
            return Response({"error": error_message}, status=response.status_code)

        # API javobini o'qish
        # Reading API
        data = response.json()
        temp_c = data['current']['temp_c']
        wind_kph = data['current']['wind_kph']
        cloud = data['current']['cloud']

        # Ranglarni aniqlash
        # Color recognition
        temp_color = self.get_weather_color(TemperatureColor, temp_c, "min_temp", "max_temp")
        wind_color = self.get_weather_color(WindColor, wind_kph, "min_wind", "max_wind")
        cloud_color = self.get_weather_color(CloudColor, cloud, "min_cloud", "max_cloud")

        # Natija
        # Result
        return Response({
            "name": data['location']['name'],
            "country": data['location']['country'],
            "lat": data['location']['lat'],
            "lon": data['location']['lon'],
            "temp_c": temp_c,
            "temp_color": temp_color,
            "wind_kph": wind_kph,
            "wind_color": wind_color,
            "cloud": cloud,
            "cloud_color": cloud_color,
        })

