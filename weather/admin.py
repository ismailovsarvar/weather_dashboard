from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, TemperatureColor, WindColor, CloudColor

admin.site.register(User)

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff')  # Ko‘rsatiladigan maydonlar # Displayed fields

admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(TemperatureColor)
class TemperatureColorAdmin(admin.ModelAdmin):
    list_display = ('temperature', 'min_temp', 'max_temp', 'color_name', 'hex_code')

@admin.register(WindColor)
class WindColorAdmin(admin.ModelAdmin):
    list_display = ('wind_speed', 'color_name', 'hex_code')

@admin.register(CloudColor)
class CloudColorAdmin(admin.ModelAdmin):
    list_display = ('cloud_coverage', 'color_name', 'hex_code')

