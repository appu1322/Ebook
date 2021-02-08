from django.contrib import admin
from .models import Stories

# Register your models here.
@admin.register(Stories)
class StoriesrAdmin(admin.ModelAdmin):
    class Media:
        js = ('inject.js',)