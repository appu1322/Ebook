from django.contrib import admin
from .models import Education

# Register your models here.
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    class Media:
        js = ('inject.js',)