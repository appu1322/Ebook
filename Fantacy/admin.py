from django.contrib import admin
from .models import Fantacy

# Register your models here.
@admin.register(Fantacy)
class FantacyAdmin(admin.ModelAdmin):
    class Media:
        js = ('inject.js',)