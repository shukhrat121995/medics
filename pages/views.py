from operator import and_
from datetime import datetime
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from functools import reduce
from .models import Person
from .generic import get_or_none
from family.models import Spouse, Children
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
    return render(request, 'pages/charts.html', {})


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
        'children': children
    }
    return render(request, 'pages/details.html', context)


def getpersons(request):
    """AJAX dynamic modal for query"""
    query = request.GET["query"]
    query = set(query.split())
    p_gender = request.GET["gender"]

    birth_from = request.GET["birth_from_date"]
    birth_to = request.GET["birth_to_date"]

    if query:
        persons = Person.objects.filter(reduce(and_, [Q(name__contains=s) for s in query])).order_by('-created_at')
    else:
        persons = Person.objects.all().order_by('-created_at')

    if p_gender:
        persons = persons.filter(gender=p_gender)

    if birth_from and birth_to:
        birth_from = datetime.strptime(birth_from, '%d/%m/%Y').strftime('%Y-%m-%d')
        birth_to = datetime.strptime(birth_to, '%d/%m/%Y').strftime('%Y-%m-%d')
        persons = persons.filter(birth__range=[birth_from, birth_to])

    paginator = Paginator(persons, 5)  # Show 1 person per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }

    return render(request, 'ajax/list_view.html', context)
