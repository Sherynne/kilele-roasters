from django.contrib import admin
from .models import Coffee, Inquiry


@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    list_display = ("name", "region", "elevation_m", "roast", "price_kes")
    list_filter = ("roast", "region")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created")
    readonly_fields = ("created",)
