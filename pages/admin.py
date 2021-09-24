from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender']
    search_fields = ['name']
    list_per_page = 50
