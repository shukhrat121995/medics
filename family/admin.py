from django.contrib import admin
from .models import Mother, Father, Spouse, Children, SocialClass


@admin.register(Father)
class FatherAdmin(admin.ModelAdmin):
    list_display = ['name', 'occupation']
    search_fields = ['name', 'occupation']
    list_per_page = 50


@admin.register(Mother)
class MotherAdmin(admin.ModelAdmin):
    list_display = ['name', 'maiden_name', 'occupation']
    search_fields = ['name', 'maiden_name', 'occupation']
    list_per_page = 50


@admin.register(Spouse)
class SpouseAdmin(admin.ModelAdmin):
    list_display = ['person', 'name', 'occupation']
    autocomplete_fields = ['person']
    search_fields = ['person__name', 'name', 'occupation']
    list_per_page = 50


@admin.register(Children)
class ChildrenAdmin(admin.ModelAdmin):
    list_display = ['person', 'name']
    autocomplete_fields = ['person']
    search_fields = ['person__name', 'name']
    list_per_page = 50


@admin.register(SocialClass)
class SocialClassAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    autocomplete_fields = ['title']
    search_fields = ['title']