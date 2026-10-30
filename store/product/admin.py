from django.contrib import admin

from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "brand",
        "price",
        "created_at",
    )

