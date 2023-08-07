from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'locations': ["Chicago", "Dallas", "Los Angeles", "Seattle", "Virginia"]
    }
    return render(request, 'index.html', context)


def create_ninja(request):
    print(request.POST)
    context = {
        "data": {
            "Name": request.POST['name'],
            "Location": request.POST['location'],
            "Language": request.POST.getlist('language'),
            # "Language": request.POST['language'],
            "Comment": request.POST['comment']
        }
    }
    print(request.POST.getlist('language'))
    for el in request.POST.getlist('language'):
        print(el)
    return render(request, 'result.html', context)
