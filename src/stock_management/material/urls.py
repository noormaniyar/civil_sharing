from django.urls import path
from .import views


app_name = 'materials'

urlpatterns = [
    path('', views.home, name='home'),
    path('material/<int:material_id>/', views.detail, name='detail'),
    path('create/inward/', views.create_inward, name='inward'),
    path('create/outward/', views.create_outward, name='outward'),

]