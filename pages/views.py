from django.shortcuts import render


def index(request):
    # Person.objects.filter(reduce(and_, [Q(name__contains=s) for s in search]))
    return render(request, 'pages/index.html', {})

