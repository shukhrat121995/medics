from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'birth', 'death', 'created_at']
    search_fields = ['name']
    list_per_page = 50
