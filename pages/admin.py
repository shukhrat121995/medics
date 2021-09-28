from django.contrib import admin
from .models import Person, Father, Mother


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'birth', 'death', 'language', 'created_at']
    search_fields = ['name']
    list_per_page = 50


@admin.register(Father)
class FatherAdmin(admin.ModelAdmin):
    list_display = ['name', 'occupation']
    search_fields = ['name']
    list_per_page = 50


@admin.register(Mother)
class MotherAdmin(admin.ModelAdmin):
    list_display = ['name', 'maiden_name', 'occupation']
    search_fields = ['name']
    list_per_page = 50