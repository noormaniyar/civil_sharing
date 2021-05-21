from django.shortcuts import render
from .models import Cloths, Inward, Outward
from django.shortcuts import get_object_or_404, render, redirect



def home(request):
    cloths_list = Cloths.objects.all()
    context = {'cloths_list':cloths_list}
    return render(request, 'cloths/home.html', context)


def detail(request, cloths_id):
    cloth = get_object_or_404(Cloths, pk=cloths_id)
    return render(request, 'cloths/detail.html', {'cloth':cloth})


