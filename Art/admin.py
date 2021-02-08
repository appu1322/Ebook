from django.contrib import admin
from .models import Art

# Register your models here.
@admin.register(Art)
class ArtAdmin(admin.ModelAdmin):
    class Media:
        js = ('inject.js',)