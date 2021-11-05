from operator import and_
from datetime import datetime
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from functools import reduce
from .models import Person
from .generic import get_or_none, life_expectancy, study_duration, practice_duration
from family.models import Spouse, Children
from career.models import Internship, DoctoralDegree, Speciality, Docentship, FirstPublicPost, HighestPost
from examinations.models import Matriculation, Premedical, CandidateOfPhilosophy, CandidateOfMedicine, \
    LicentiateOfPhilosophy, Dispensation, Legislation


def index(request):
    persons = Person.objects.all().order_by('-created_at')
    context = {
        'persons': persons
    }
    return render(request, 'pages/base.html', context)


def about(request):
    return render(request, 'pages/about.html', {})


def charts(request):
    graduates = Person.objects.select_related(None)
    male = graduates.filter(gender='Male').all()
    female = graduates.filter(gender='Female').all()

    premedical = Premedical.objects.select_related('person')
    licentiate = LicentiateOfPhilosophy.objects.select_related('person')

    doctorates = DoctoralDegree.objects.all()
    docents = Docentship.objects.all()

    context = {
        'graduates': graduates.count(),
        'male': male.count(),
        'female': female.count(),
        'avr_life': life_expectancy(graduates),
        'avr_life_male': life_expectancy(male),
        'avr_life_female': life_expectancy(female),

        'avr_med_study': study_duration(graduates, premedical, licentiate),
        'avr_med_study_male': study_duration(graduates.filter(gender='Male'), premedical, licentiate),
        'avr_med_study_female': study_duration(graduates.filter(gender='Female'), premedical, licentiate),

        'avr_med_practice': practice_duration(graduates),
        'avr_med_practice_male': practice_duration(male),
        'avr_med_practice_female': practice_duration(female),

        'doctorate_and_docent': doctorates.count() + docents.count(),
        'doctorate_male': doctorates.filter(person__gender='Male').count(),
        'doctorate_female': doctorates.filter(person__gender='Female').count(),
        'docent_male': docents.filter(person__gender='Male').count(),
        'docent_female': docents.filter(person__gender='Female').count()
    }
    return render(request, 'pages/charts.html', context)


def details(request, pk):
    person = get_or_none(Person, pk=pk)
    matriculation = get_or_none(Matriculation, person=pk)
    premedical = get_or_none(Premedical, person=pk)
    candidate_of_philosophy = get_or_none(CandidateOfPhilosophy, person=pk)
    candidate_of_medicine = get_or_none(CandidateOfMedicine, person=pk)
    licentiate_of_medicine = get_or_none(LicentiateOfPhilosophy, person=pk)
    dispensation = get_or_none(Dispensation, person=pk)
    legislation = get_or_none(Legislation, person=pk)
    spouses = Spouse.objects.filter(person=pk).all()
    children = Children.objects.filter(person=pk).all()
    internships = Internship.objects.filter(person=pk).all()
    doctoral_degrees = DoctoralDegree.objects.filter(person=pk).all()
    specialities = Speciality.objects.filter(person=pk).all()
    docentships = Docentship.objects.filter(person=pk).all()
    first_public_post = get_or_none(FirstPublicPost, person=pk)
    highest_post = get_or_none(HighestPost, person=pk)

    context = {
        'person': person,
        'matriculation': matriculation,
        'premedical': premedical,
        'candidate_of_philosophy': candidate_of_philosophy,
        'candidate_of_medicine': candidate_of_medicine,
        'licentiate_of_medicine': licentiate_of_medicine,
        'dispensation': dispensation,
        'legislation': legislation,
        'spouses': spouses,
        'children': children,
        'internships': internships,
        'doctoral_degrees': doctoral_degrees,
        'specialities': specialities,
        'docentships': docentships,
        'first_public_post': first_public_post,
        'highest_post': highest_post
    }
    return render(request, 'pages/details.html', context)


def getpersons(request):
    """AJAX dynamic modal for query"""
    query = request.GET["query"]
    query = set(query.split())
    p_gender = request.GET["gender"]

    p_language = request.GET["language"]

    p_social_class = request.GET["social_class"]

    p_place_of_birth = request.GET["place_of_birth"]

    birth_from = request.GET["birth_from_date"]
    birth_to = request.GET["birth_to_date"]
    death_from = request.GET["death_from_date"]
    death_to = request.GET["death_to_date"]

    if query:
        persons = Person.objects.filter(reduce(and_, [Q(name__icontains=s) for s in query])).order_by('-created_at')
    else:
        persons = Person.objects.all().order_by('-created_at')

    if p_gender:
        persons = persons.filter(gender=p_gender)

    if p_language:
        persons = persons.filter(language=p_language)

    if p_social_class:
        persons = persons.filter(social_class__title=p_social_class)

    if p_place_of_birth:
        persons = persons.filter(place_of_birth__icontains=p_place_of_birth)

    if birth_from and birth_to:
        birth_from = datetime.strptime(birth_from, '%d/%m/%Y').strftime('%Y-%m-%d')
        birth_to = datetime.strptime(birth_to, '%d/%m/%Y').strftime('%Y-%m-%d')
        persons = persons.filter(birth__range=[birth_from, birth_to])

    if death_from and death_to:
        death_from = datetime.strptime(death_from, '%d/%m/%Y').strftime('%Y-%m-%d')
        death_to = datetime.strptime(death_to, '%d/%m/%Y').strftime('%Y-%m-%d')
        persons = persons.filter(death__range=[death_from, death_to])

    paginator = Paginator(persons, 25)  # Show 1 person per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }

    return render(request, 'ajax/list_view.html', context)
