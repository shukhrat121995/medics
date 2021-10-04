from django.contrib import admin
from .models import Person, Father, Mother, Spouse, Children


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'birth', 'death', 'language', 'created_at']
    autocomplete_fields = ['father', 'mother']
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


@admin.register(Spouse)
class SpouseAdmin(admin.ModelAdmin):
    list_display = ['person', 'name', 'occupation']
    autocomplete_fields = ['person']
    search_fields = ['person', 'name', 'occupation']
    list_per_page = 50


@admin.register(Children)
class ChildrenAdmin(admin.ModelAdmin):
    list_display = ['person', 'name']
    autocomplete_fields = ['person']
    search_fields = ['person', 'name']
    list_per_page = 50