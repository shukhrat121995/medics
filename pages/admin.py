from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    @admin.display(ordering='matriculation__date')
    def matriculation_exam(self, obj):
        return obj.matriculation.date

    @admin.display(ordering='licentiateofphilosophy__date')
    def licentiate_of_medicine_exam(self, obj):
        return obj.licentiateofphilosophy.date

    list_display = ['name',
                    'gender',
                    'birth',
                    'death',
                    'language',
                    'matriculation_exam',
                    'licentiate_of_medicine_exam',
                    'created_at'
                    ]
    autocomplete_fields = ['father', 'mother']
    search_fields = ['name']
    list_per_page = 50
