from django.contrib import admin
from .models import Bestseller

# Register your models here.

@admin.register(Bestseller)
class BestsellerAdmin(admin.ModelAdmin):
    class Media:
        js = ('inject.js',)