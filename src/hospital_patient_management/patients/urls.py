from django.urls import path
from . import views


app_name = 'patient'

urlpatterns = [
    path('', views.home, name='home'),
    path('patient_detail/<int:patient_id>/', views.patient_detail, name='patient_detail'),
    path('discharged_patients', views.discharged_patients, name='discharged_patients'),
    path('creating_discharge', views.creating_discharge, name='creating_discharge'),
    path('creating_bed', views.BedCreateView.as_view(), name='creating_bed'),
    path('creating_patient', views.creating_patient, name='creating_patient'),
    path('edit_patient/<int:patient_id>/', views.edit_patient, name='edit_patient'),
    path('beds/', views.bed, name='bed_list'),
    path('all_patients_detail/', views.all_patients_detail, name='all_patients_detail'),
    path('register/', views.register, name='register'),

]