from django.contrib import admin
from .models import Internship, Docentship, DoctoralDegree, FirstPublicPost, HighestPost, Speciality


@admin.register(Internship)
class AdminInternship(admin.ModelAdmin):
    list_display = ['person', 'start_date', 'end_date', 'name_of_clinic_or_department']
    autocomplete_fields = ['person']
    search_fields = ['person__name']
    list_per_page = 50


@admin.register(DoctoralDegree)
class AdminDoctoralDegree(admin.ModelAdmin):
    list_display = ['person', 'date', 'field_of_doctorate']
    autocomplete_fields = ['person']
    search_fields = ['person__name']
    list_per_page = 50


@admin.register(Speciality)
class AdminSpeciality(admin.ModelAdmin):
    list_display = ['person', 'date', 'name_of_speciality']
    autocomplete_fields = ['person']
    search_fields = ['person__name']
    list_per_page = 50


@admin.register(Docentship)
class AdminDocentship(admin.ModelAdmin):
    list_display = ['person', 'date', 'name_of_docentship']
    autocomplete_fields = ['person']
    search_fields = ['person__name']
    list_per_page = 50


@admin.register(FirstPublicPost)
class AdminFirstPublicPost(admin.ModelAdmin):
    list_display = ['person', 'date', 'name_of_post']
    autocomplete_fields = ['person']
    search_fields = ['person__name']
    list_per_page = 50


@admin.register(HighestPost)
class AdminHighestPost(admin.ModelAdmin):
    list_display = ['person', 'date', 'name_of_post']
    autocomplete_fields = ['person']
    search_fields = ['person__name']
    list_per_page = 50