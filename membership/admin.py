from django.contrib import admin
from .models import MemberOfFls, MemberOfDuodecim


@admin.register(MemberOfFls)
class AdminMemberOfFls(admin.ModelAdmin):
    list_display = ['person', 'start_date', 'end_date']
    autocomplete_fields = ['person']
    search_fields = ['person__name']
    list_per_page = 50


@admin.register(MemberOfDuodecim)
class AdminMemberOfDuodecim(admin.ModelAdmin):
    list_display = ['person', 'start_date', 'end_date']
    autocomplete_fields = ['person']
    search_fields = ['person__name']
    list_per_page = 50
