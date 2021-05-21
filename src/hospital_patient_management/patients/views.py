from .models import Patient, Bed
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BedCreateForm
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy


class BedCreateView(LoginRequiredMixin, CreateView):

    model = Bed
    template_name = 'patient/creating_bed.html'
    fields = ['bed_name', 'extra_info']
    success_url = reverse_lazy('patient:home')

    def form_valid(self, form):
        messages.success(self.request, 'New Bed has been created successfully!')
        return super().form_valid(form)


def register(request):
    form=UserCreationForm
    if request.method=='POST':
        regForm=UserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            messages.success(request, 'User Has Been Registered Successfully...')
    return render (request, 'registration/register.html', {'form':form})

@login_required
def home(request):
    patient_list = Patient.objects.filter(is_discharge=False).order_by('-hospitalized_on')
    bed_list = Bed.objects.all()
    empty_beds = Bed.objects.filter(patient=None)
    context = {'patient_list': patient_list, 'bed_list': bed_list, 'empty_beds': empty_beds}
    return render(request, 'patient/home.html', context)


@login_required
def bed(request):
    bed_list = Bed.objects.all()
    patient_list = Patient.objects.all()
    empty_beds = Bed.objects.filter(patient=None)

    context = {'bed_list':bed_list, 'patient_list':patient_list, 'empty_beds': empty_beds}
    return render(request, 'patient/bed_list.html', context)


@login_required
def all_patients_detail(request):
    all_patient = Patient.objects.all().order_by('-hospitalized_on','is_discharge','-discharged_on')
    bed_list = Bed.objects.all()

    context = {'all_patient': all_patient, 'bed_list' : bed_list}
    return render(request, 'patient/all_patients_detail.html', context)


@login_required
def patient_detail(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    context = {'patient': patient}
    return render(request, 'patient/patient_detail.html', context)

@login_required
def creating_bed_old(request):
    if request.method == "POST":
        bed_name_from_post = request.POST['bed_name123']
        bed_extra_info_from_post = request.POST['bed_extra_info123']
        new_bed = Bed.objects.create(bed_name=bed_name_from_post, extra_info=bed_extra_info_from_post)
        print(new_bed)
        messages.success(request, 'new Bed has been created successfully!')
        return redirect('patient:home')
    else:
        return render(request, 'patient/creating_bed.html')

@login_required
def creating_bed(request):
    if request.method == "POST":
        form = BedCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'new Bed has been created successfully!')
            return redirect('patient:home')
        else:
            print(form.errors)
            context = {'form': form}
            return render(request, 'patient/creating_bed.html', context)
    else:
        form = BedCreateForm()
        context = {'form': form}
        return render(request, 'patient/creating_bed.html', context)



@login_required
def creating_patient(request):
    if request.method == "POST":
        bed_id = request.POST['bed_id']
        pat_name_from_post = request.POST['full_name']
        bed = Bed.objects.get(id=bed_id)
        pat_treatment_from_post = request.POST['treatment']
        pat_extra_info_from_post = request.POST['extra_info']
        new_patient = Patient.objects.create(full_name=pat_name_from_post, treatment=pat_treatment_from_post, extra_info=pat_extra_info_from_post, bed=bed)
        print(new_patient)
        return redirect('patient:home')
    else:
        beds = Bed.objects.filter(patient=None)
        context = {'beds': beds}
        return render(request, 'patient/creating_patient.html', context)


@login_required
def edit_patient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    if request.method == "POST":
        bed_id = request.POST['bed_id']
        bed = Bed.objects.get(id=bed_id)
        pat_extra_info_from_post = request.POST['extra_info']
        patient.bed = bed
        patient.extra_info = pat_extra_info_from_post
        patient.save()
        return redirect('patient:home')
    else:
        beds = Bed.objects.filter(patient=None)
        context = {'beds': beds, 'patient': patient}
        return render(request, 'patient/edit_patient.html', context)


@login_required
def creating_discharge(request):
    if request.method == "POST":
        patient_id = request.POST['patient_id']
        pat_bill_from_post = request.POST['bill']
        patient = Patient.objects.get(id=patient_id)
        patient.bill = pat_bill_from_post
        patient.is_discharge = True
        patient.bed = None
        patient.discharged_on = timezone.now()
        patient.save()
        return redirect('patient:discharged_patients')
    else:
        patients = Patient.objects.filter(is_discharge=False)
        context = {'patients': patients}
        return render(request, 'patient/creating_discharge.html', context)


@login_required
def discharged_patients(request):
    patient_list = Patient.objects.filter(is_discharge=True).order_by('-discharged_on')
    bed_list = Bed.objects.all()

    context = {'patient_list': patient_list, 'bed_list': bed_list}
    return render(request, 'patient/discharged_patients.html', context)



