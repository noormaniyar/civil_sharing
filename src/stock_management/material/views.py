from django.http import HttpResponse
from .models import Material, Inward, Outward
from django.shortcuts import get_object_or_404, render, redirect
import datetime
from django.utils import timezone


def home(request):
    material_list = Material.objects.all()
    context = {'material_list':material_list}
    return render(request, 'material/home.html', context)


def detail(request, material_id):
    mat = get_object_or_404(Material, pk=material_id)
    return render(request, 'material/detail.html', {'mat': mat})


def create_inward(request):
    if request.method == "POST":
        material_id = request.POST['material_id']
        material = Material.objects.get(id=material_id)
        weight = int(request.POST['weight'])
        inward = Inward.objects.create(material=material, weight=weight)
        return redirect('materials:home')
    else:
        materials = Material.objects.all()
        context = {'materials': materials}
        return render(request, 'material/create_inward.html', context)


def create_outward(request):
    if request.method == "POST":
        material_id = request.POST['material_id']
        material = Material.objects.get(id=material_id)
        weight = int(request.POST['weight'])
        outward = Outward.objects.create(material=material, weight=weight)
        return redirect('materials:home')
    else:
        materials = Material.objects.all()
        context = {'materials': materials}
        return render(request, 'material/create_outward.html', context)