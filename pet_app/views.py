from django.shortcuts import render
from django.http import HttpResponse
from .models import Pets
from django.http import Http404


def home(request):
    pets = Pets.objects.all()
    return render(request, 'home.html', {'pets': pets})

# return HttpResponse('<p>home view</p>')


def pet_detail(request, id):
    try:
        pet = Pets.objects.get(id=id)
    except Pets.DoesNotExist:
        raise Http404('pet not found')
    return render(request, 'pet_detail.html', {'pet':pet})

# return HttpResponse('<p>pet_Detail with the id {}</p>'.format(id))