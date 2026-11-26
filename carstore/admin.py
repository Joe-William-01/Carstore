from django.contrib import admin
from .models import Cars


@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ("model", "color", "price", "invented_year")