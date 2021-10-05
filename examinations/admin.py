from django.contrib import admin
from .models import Matriculation, Premedical, CandidateOfPhilosophy, CandidateOfMedicine, LicentiateOfPhilosophy, \
    Legislation, Dispensation


@admin.register(Matriculation)
class AdminMatriculation(admin.ModelAdmin):
    list_display = ['person', 'date', 'school', 'grade']
    autocomplete_fields = ['person']
    search_fields = ['person']
    list_per_page = 50


@admin.register(Premedical)
class AdminPremedical(admin.ModelAdmin):
    list_display = ['person', 'date', 'school', 'grade']
    autocomplete_fields = ['person']
    search_fields = ['person']
    list_per_page = 50


@admin.register(CandidateOfPhilosophy)
class AdminCandidateOfPhilosophy(admin.ModelAdmin):
    list_display = ['person', 'date', 'school', 'grade']
    autocomplete_fields = ['person']
    search_fields = ['person']
    list_per_page = 50


@admin.register(CandidateOfMedicine)
class AdminCandidateOfMedicine(admin.ModelAdmin):
    list_display = ['person', 'date', 'school', 'grade']
    autocomplete_fields = ['person']
    search_fields = ['person']
    list_per_page = 50


@admin.register(LicentiateOfPhilosophy)
class AdminLicentiateOfPhilosophy(admin.ModelAdmin):
    list_display = ['person', 'date', 'school', 'grade']
    autocomplete_fields = ['person']
    search_fields = ['person']
    list_per_page = 50


@admin.register(Legislation)
class AdminLegislation(admin.ModelAdmin):
    list_display = ['person', 'date', 'school', 'grade']
    autocomplete_fields = ['person']
    search_fields = ['person']
    list_per_page = 50


@admin.register(Dispensation)
class AdminDispensation(admin.ModelAdmin):
    list_display = ['person', 'date', 'school', 'grade']
    autocomplete_fields = ['person']
    search_fields = ['person']
    list_per_page = 50
