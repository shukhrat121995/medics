from operator import and_

from django.db.models import Q
from django.shortcuts import render
from functools import reduce
from .models import Person


def index(request):
    persons = Person.objects.all().order_by('-created_at')
    context = {
        'persons': persons
    }
    return render(request, 'pages/index.html', context)


def getpersons(request):
    """AJAX dynamic modal for query"""
    if request.method == "GET":
        query = request.GET["query"]
        query = set(query.split())
        if query:
            persons = Person.objects.filter(reduce(and_, [Q(name__contains=s) for s in query])).order_by('-created_at')
        else:
            persons = Person.objects.all().order_by('-created_at')

        context = {
            'persons': persons
        }

        return render(request, 'ajax/list_view.html', context)

